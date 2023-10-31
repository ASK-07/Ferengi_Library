#!/usr/bin/env python -B
import sys 
sys.dont_write_bytecode = True
from flask import Flask, render_template
from chess_engine import Engine

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

@app.route('/move/<int:depth>/<path:fen>/')
def get_move(depth, fen):
    print(depth)
    print("Calculating...")
    engine = Engine(fen)
    move = engine.iterative_deepening(depth - 1)
    print("Move found!", move)
    print()
    return move

@app.route('/test/<string:tester>')
def test_get(tester):
    return tester
    

if __name__ == '__main__':
  app.run(debug=True)
