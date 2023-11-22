'''
    This module initializes the flask app and configures extensions

'''
from flask import Flask, app
from .mongo_config import mongo

from pymongo import MongoClient

app = Flask(__name__, static_url_path='', static_folder='static',template_folder='templates')

app.config["MONGO_URI"] = 'mongodb+srv://Heath:VsaClEbzM7VkaUuQ@dev-aws-website.ppvg8ly.mongodb.net/Games?retryWrites=true&w=majority'

mongo.init_app(app)

from .routes import routes_app
app.register_blueprint(routes_app)

from Flask_Game_Host import routes