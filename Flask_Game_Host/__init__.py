'''
    This module initializes the flask app and configures extensions

'''
from dotenv import load_dotenv
from flask import Flask, app
import flask
from flask_pymongo import PyMongo
import os
#app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='static',template_folder='templates')

# Authenticate connection to db
app.config['MONGO_URI'] = 'mongodb+srv://Ferengi:OCCzIyeq9mjl7YwM@dev-aws-website.ppvg8ly.mongodb.net/?retryWrites=true&w=majority'

mongodb_client = PyMongo(app)
db = mongodb_client.db

from Flask_Game_Host import routes