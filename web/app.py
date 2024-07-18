from flask import Flask, render_template, request, redirect
import sqlite3
from colorama import Fore, Back, Style

# con = sqlite3.connect("static/sydney.db")
# cur = con.cursor()

app = Flask(__name__)

# "public" variables

@app.route("/")

def hello_world():
    return render_template("chat.html")