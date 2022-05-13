from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "secret key"
app.config["MONGO_URI"] = "mongodb+srv://flask:flask@flask.sgsvz.mongodb.net/CN"
mongo = PyMongo(app)


