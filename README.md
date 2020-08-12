# NetDucky
A wifi enabled key injector, that gets instructions from a flask server


Run Server: 
Run server with following set of commands

        cd server_app
        gunicorn --bind <IP>:<PORT> app:server_app