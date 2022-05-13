from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init app
app = Flask(__name__)

@app.route("/display", methods = ["GET"])
def Welcome():
    return({"message" : "Welcome!"})

#run server
if __name__ == "__main__":
    app.run(debug=True)