import os
from flask import Flask, app        # Ensure no bugs from importing app
from .mongo_config import mongo   # Unsure if necessary, works without
from dotenv import load_dotenv

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

# Put key in .env/ sys env var
load_dotenv() 
app.config["MONGO_URI"] = 'mongodb+srv://Heath:VsaClEbzM7VkaUuQ@dev-aws-website.ppvg8ly.mongodb.net/Games?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') 

mongo.init_app(app)

from .routes import routes_app
app.register_blueprint(routes_app)

#from Flask_Game_Host import routes   