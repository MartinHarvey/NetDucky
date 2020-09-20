import os
from flask import request
from app import server_app


#Basic route. Used to test if server is running and responding to requests
@server_app.route('/')
@server_app.route('/index')
def index():
    return "Hello, World!"

# <duckey_name> corresponds to the name each ducky client has. This allows you 
# to issue different instructions to 
# different duckys. 
@server_app.route('/download/<duckey_name>', methods = ['GET'])
def file_Page(duckey_name):
    path = os.getcwd() +"/files/" + duckey_name
    with open(path, "r") as file:
        data = file.read()
        file.close()
    return(data, 200)

#Upload a new set of instructions for <ducky_name>. 
@server_app.route('/upload/instructions/<ducky_name>/', methods = ['POST'])
def upload_Instruction(ducky_name):
    file = request.files['secret']
    file.save(os.path.join(server_app.config['UPLOAD_FOLDER'], ducky_name))
    return ("Success", 200)




