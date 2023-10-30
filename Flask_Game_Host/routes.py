#!/usr/bin/env python -B
import sys 
sys.dont_write_bytecode = True
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('homepage.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/game')
def game():
  return render_template('game.html')

if __name__ == '__main__':
  app.run(debug=True)
