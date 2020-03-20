from flask import Flask, request, jsonify, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle
from blinker import signal

boggle_game = Boggle()

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
# app.config['TESTING'] = True

debug = DebugToolbarExtension(app)


@app.route("/")
def render_board():
    board = boggle_game.make_board()
    return render_template("board.html", board=board)

@app.route('/check-word')
def check_word():