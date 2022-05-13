from flask import Flask, jsonify, render_template
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

data = {"name": "Dave Lyndrex Millan", "age": 20}

@app.route("/")
def myname():
    return render_template('../index.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)

