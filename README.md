# NetDucky
A wifi enabled key injector, that gets instructions from a flask server


Run Server: 
Run server with following set of commands

        cd server_app
        gunicorn --bind <IP>:8000 app:server_app
        
The current version of the key injector software runs specifically on a Raspberry Pi Pico connected to a Pimoroni Wireless Pack, and uses the latest version of the Circuitpython UF2. The code requires that the Circuitpython adafruit_esp32spi, adafruit_hid and adafruit_requests libraries inside the lib folder of the CIRCUITPY drive. Other ESP32 based add-on boards (and other HID capable circuitpython microcontrollers) can be used, but with edits to the code describing the pins the ESP32 is connected to. 

The ```secrets.py``` file must also include the SSID and password of the network you are connecting to, the IP address of the machine running the flask app, and the name of the ducky. The ducky name will dictate what instructions the ducky gets. So "Ducky1" will get the file called "Ducky1". A basic secrets file is provided with example data.

Instruction files are made up of the following statements:
* STRING [string] :- Text for the ducky to type out. For example "STRING Hello" would type out "Hello"
* WIN :- Presses the Windows/Super/Command key
* ENTER :- Sends the Enter key. 
* WAIT [interval] :- Waits a set amount of time. Interval must be a float i.e. WAIT 0.5 will wait 0.5 seconds

Abilty to send CTRL-Key combinations (CTRL+S, CTRL+R) is being worked on. 



