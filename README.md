# NetDucky
A wifi enabled key injector, that gets instructions from a flask server


Run Server: 
Run server with following set of commands

        cd server_app
        gunicorn --bind <IP>:<PORT> app:server_app
        
Currently not being worked on owing to lack of USB-HID library support for the ESP32-S2. Hopefully will pick up again when the availability of the S2 picks up and software ecosystem matures. 
