import os
from flask import request
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
def file_Page(duckey_name):
    path = os.getcwd() +"/files/" + duckey_name
    with open(path, "r") as file:
        data = file.read()
        file.close()
    return(data, 200)

#Upload a new set of instructions for <ducky_name>. 
@app.route('/upload/instructions/<ducky_name>/', methods = ['POST'])
def upload_Instruction(ducky_name):
    file = request.data
    path = os.getcwd() +"/files/" + ducky_name
    with open(path, "w") as f:
        f.write(file)
        print(f)
        f.close()
        return "Success"




