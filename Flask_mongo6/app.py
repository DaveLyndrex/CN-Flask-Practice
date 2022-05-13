from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'CN'
app.config['MONGO_URI'] ='mongodb+srv://flask:flask@flask.sgsvz.mongodb.net/CN'

mongo = PyMongo(app)

#retrieve data
@app.route('/intern', methods=['GET'])
def get_all_intern():
    intern = mongo.db.intern 

    output = []

    for query in intern.find():
        output.append({'name' : query['name'], 'position' : query['position']})

    return jsonify({'result' : output})

#specific
@app.route('/intern/<name>', methods=['GET'])
def get_one_intern(name):
    intern = mongo.db.intern

    query = intern.find_one({'name' : name})

    if query:
        output = {'name' : query['name'], 'position' : query['position']}
    else:
        output = 'No results found'

    return jsonify({'result' : output})


#add
@app.route('/intern', methods=['POST'])
def add_intern():
    intern = mongo.db.intern 

    name = request.json['name']
    position = request.json['position']

    intern_id = intern.insert({'name' : name, 'position' : position})
    new_intern = intern.find_one({'_id' : intern_id})

    output = {'name' : new_intern['name'], 'position' : new_intern['position']}

    return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(debug=True)