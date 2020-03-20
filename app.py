from flask import Flask, request, jsonify, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle
from blinker import signal

boggle_game = Boggle()

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
# app.config['TESTING'] = True

debug = DebugToolbarExtension(app)

BOARD = []

@app.route("/")
def render_board():
    BOARD = boggle_game.make_board()
    return render_template("board.html", board=BOARD)


@app.route('/check-word')
def check_word():
    word = request.args["word-submission"]
    result = boggle_game.check_valid_word(BOARD, word)

    if result == "ok":
        
    # if word_exists and valid_word:
    #         result = "ok"
    #     elif word_exists and not valid_word:
    #         result = "not-on-board"
    #     else:
    #         result = "not-word"


