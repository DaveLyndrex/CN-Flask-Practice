from flask import Flask, render_template, url_for, request, session, redirect
import pymongo
import bcrypt

app = Flask(__name__)


##########################################################################################################
try:
    #connect to mongo
    mongo = pymongo.MongoClient(host="localhost", 
    port=27017, 
    serverSelectionTimeoutMS = 1000) #serverSelec.... will allow us to catch exception
    
    #creating database variable, connecting to mongo client and the database we want to use
    db = mongo.cloud_ninja
    mongo.server_info()#trigger exception if cannot connect to database
except:
    print("ERROR = Cannot connect to db")


#########################################################################################################################

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as' + session['username']

    return render_template('index.html')

@app.route('/login')
def login():
    return ''

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
            
        return 'That username already exists!'
    
    return render_template('register.html')

if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(debug=True)