# NetDucky
A wifi enabled key injector, that gets instructions from a flask server


## Run Server

Run server with following set of commands

        cd server_app
        gunicorn --bind <IP>:8000 app:server_app

## Key Injectors        
The current version of the key injector software runs specifically on a Raspberry Pi Pico connected to a Pimoroni Wireless Pack, and uses the latest version of the Circuitpython UF2. The code requires that the Circuitpython adafruit_esp32spi, adafruit_hid and adafruit_requests libraries inside the lib folder of the CIRCUITPY drive. Other ESP32 based add-on boards (and other HID capable circuitpython microcontrollers) can be used, but with edits to the code describing the pins the ESP32 is connected to. 

The ```secrets.py``` file must also include the SSID and password of the network you are connecting to, the IP address of the machine running the flask app, and the name of the ducky. The ducky name will dictate what instructions the ducky gets. So "Ducky1" will get the file called "Ducky1". A basic secrets file is provided with example data.

The RGB LED connected to the ESP32 will change colour as the key injector runs. Red means that the Injector is not connected to any wireless network. It turns green when its connected to a network, and carrying out the main code (getting instructions and carrying them out), before turning blue when the code has finished running, and all instructions are carried out.  

## Instruction Files
Instruction files are made up of the following statements:
* STRING [string] :- Text for the ducky to type out. For example "STRING Hello" would type out "Hello"
* WIN :- Presses the Windows/Super/Command key
* ENTER :- Sends the Enter key. 
* WAIT [interval] :- Waits a set amount of time. Interval must be a float i.e. WAIT 0.5 will wait 0.5 seconds
* CTRL [keys] :- Allows you to send a control-key combination. For example, CTRL+S

Instruction files are stored in the files directory of the server_app

Other features are in the works, but the current functionality is sufficient to build up instruction scripts that can carry out a great deal of work



### Disclaimer
Do not, under any circumstances, use this software to commit a crime. Only use the software on devices and networks you have permission to. 

