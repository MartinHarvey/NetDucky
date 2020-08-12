from flask import Flask


server_app = Flask(__name__)

UPLOAD_FOLDER = 'files'
server_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes

