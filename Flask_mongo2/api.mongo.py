from flask import Flask
from flask_mongoengine import MongoEngine
from api_constants import mongodb_password

app = Flask(__name__)

database_name = "CN"
DB_URI = "mongodb+srv://flask:flask@flask.sgsvz.mongodb.net/CN"
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)

class Book(db.Document):
    book_id = db.IntField()
    name = db.StringField()
    author = db.StringField()
    
    def to_json(self):
        #converts this document to JSON
        return {
            "book_id" : self.book_id,
            "name" : self.name,
            "author" : self.author
        }

'''
HTTP method for API does:
POST /api/db_populate => Populates the db nad returns 201 success code (empty response body)
'''

@app.route('/api/db_populate', methods=['POST'])
def db_populate():
    book1 = Book(book_id=1, name="Game of Thrones", author="George RR Martin")
    book2 = Book(book_id=2, name="Lord of the Rings", author="JRR Tolkien")
    book1.save()
    book2.save()

'''
GET /api/books => Return the details of all books (eith code 200 success code)
POST /api/books => Creates a new book and returns 201 success code (empty response body)
GET /api/books/3 => Returns the details of the book 3 (with 200 success code if document found, 404 if not found)
PUT /api/books/3 => Update author and name fields of book 3 (with 204 success code)
DELETE /api/books/3 => Deletes book 3 (with 204 success code)
'''



@app.route('/api/db_books', methods=['GET'])
def api_books():
    pass

@app.route('/api/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_book(book_id):
    pass

if __name__ == "__main__":
    app.run(debug=True)