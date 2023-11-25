import os
from flask import Flask, app        # Ensure no bugs from importing app
# from .mongo_config import mongo   # Unsure if necessary, works without
from pymongo import MongoClient
from dotenv import load_dotenv

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

# Configure flask app extensions
load_dotenv()
uri = os.getenv('MONGO_URI')

app.config['MONGO_URI'] = uri
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Put key in .env/ sys env var
# app.config["MONGO_URI"] = 'mongodb+srv://Heath:VsaClEbzM7VkaUuQ@dev-aws-website.ppvg8ly.mongodb.net/Games?retryWrites=true&w=majority'

# Establish connection to database
mongodb_client = MongoClient(uri)
db = mongodb_client['Games']

# mongo.init_app(app)

score_data = [
    {'player_name' : "Heath",'score' : 12000},
    {'player_name' : "Jake",'score' : 14000},
    {'player_name' : "Nathan",'score' : 15000},
    {'player_name' : "Alex",'score' : 15000},
    {'player_name' : "Jaime",'score' : 15001}
]

# This adds 5 documents to HostedGames every time app is ran... There are 700 documents in the collection
# Also consider changing collection name to Scores
# mongo.db.HostedGames.insert_many(score_data)

from .routes import routes_app
app.register_blueprint(routes_app)

# from Flask_Game_Host import routes    # Likely unnecessary