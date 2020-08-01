#import Flask class from the flask module
from flask import Flask
#import SQLAlchemy class from flask_sqlalchemy module
from flask_sqlalchemy import SQLAlchemy
#import os module
import os
# create a new instance of Flask and store it in app 
app = Flask(__name__)
#creating environment variable that will allow us to provide value for application configuration with db
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)
# import the ./application/routes.py file
from application import routes
