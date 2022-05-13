from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

#instantiate flask app
app = Flask(__name__)

#@app.route("/todolist")
#def todo():
    #return({"Message" : "This is a get request!"})

#set configs set up
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#instantiate db object
db = SQLAlchemy(app)

#create a marshmallow object
ma = Marshmallow(app)

#create database
class TodoList(db.Model):
    #creating columns in flask
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.id

#Creating todolist schema
class TodolistSchema(ma.Schema):
    class Meta:
        #exposing fields
        fields = ('id', 'name', 'description', 'completed', 'date_time')

#creating instance of schemas
#an object of TodolistSchema
todolist_schema = TodolistSchema(many = False)
todolists_schema = TodolistSchema(many = True)



#creating  todos route
@app.route("/todolist", methods=["POST"])#post allows users to create something in the database

def add_todo():
    try:
        name = request.json['name']
        description = request.json['description']

        new_todo = TodoList(name = name , description = description)
        
        #add to database
        db.session.add(new_todo)#tell the database that we want to perform changes
        db.session.commit()#the changes is permanently written in the database

        return todolist_schema.jsonify(new_todo)

    except Exception as e:
        return jsonify({"Error" : "Invalid request!"})#return to the user in a json format


#get todos
@app.route("/todolist", methods = ["GET"])
def get_todos():
    todos =TodoList.query.all()
    result_set = todolists_schema.dump(todos)


@app.route("/todolist/<int:id>", methods = ["GET"])
def get_todo(id):
    todo = TodoList.query.get_or_404(int(id))
    return todolist_schema.jsonify(todo)


#update todo
@app.route("/todolist/<int:id>", methods = ["PUT"])
def update_todo(id):
    todo = TodoList.query.get_or_404(int(id))

    name = request.json['name']
    description = request.json['description']
    completed = request.json['completed']

    todo.name = name
    todo.decription = description
    todo.completed = completed

    db.session.commit()
    return todolist_schema(todo)


#delete todo
@app.route("/todolist/<int:id>", methods = ["DELETE"])
def delete_todo(id):
    todo = TodoList.query.get_or_404(int(id))
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"Success" : "Todo deleted!"})


if __name__ == "__main__":
    app.run(debug=True)