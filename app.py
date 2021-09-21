from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import json
con = sqlite3.connect('users.db')

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = con

db = SQLAlchemy(app)

