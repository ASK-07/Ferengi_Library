import os
from flask import Flask, app
from .mongo_config import mongo
from dotenv import load_dotenv

# Initialize flask app
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

# Configure flask extensions
load_dotenv() 
app.config["MONGO_URI"] = os.getenv("MONGO_URI") 
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') 

# Integrate MongoDB with flask app
mongo.init_app(app)

from .routes import routes_app
app.register_blueprint(routes_app)
 