from flask import Flask, render_template,request, json, redirect, session
from flask_mongoengine import MongoEngine
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "12345678"

############################################# D A T A B A S E ##################################################### 
app.config['MONGODB_SETTINGS'] = {
    'db' : 'cloud_ninja',
    'host' : 'localhost',
    'port' : 27017
}

db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    reg_date = db.DateTimeField(datetime.now)



@app.route('/')
def main():
    return render_template('index.html')


############################################### S I G N  U P ##################################################### 
@app.route('/signup/', methods=['POST', 'GET'])
def signup():
    today = datetime.today()
    print(today)
    if request.method == 'POST':
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        #validate the received values
        if _name and _email and _password:
            _hashed_password = generate_password_hash(_password)
            users = User.objects(email = _email).first()
            if not users:
                usersave = User(name=_name, email=_email, password=_hashed_password, reg_date=today)
                usersave.save() #or
                #user.insert_one(usersave)
                msg = '{ "html" : "OK"}'
                msghtml = json.loads(msg)
                return msghtml("html")
            else:
                msg = '{ "html":"<h3>user with this email address already exists</h3>"}'
                msghtml = json.loads(msg)
                return msghtml["html"]
        else:
            msg = '{ "html":"<h3>Enter required fields</h3>"}'
            msghtml = json.loads(msg)
            return msghtml["html"]

    else:
        return render_template('signup.html')





################################################### L O G I N ##########################################################
@app.route('/login', methods=['GET', 'POST'])
def login():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

    if request.method == 'POST':
        #GET FORM FIELDS
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

        #GET USER BY USERNAME
        users = User.objects(email = _username).count()
        print(users) #result 1

        if users > 0:
            #GET STORED HASH
            user_rs = User.objects(email = _username).first()
            password = user_rs['password']
            print(password)
            #COMPARE PASSWORDS
            if check_password_hash(password, _password):
                #PASSED
                session['sessionusername'] = _username
                return redirect('/userHome')
                

            else:
                error = 'Invalid Login'
                return render_template('signin.html', error = error)

        else:
            error = 'Username not found'
            return render_template('signin.html', error=error)

    return render_template('signin.html')


############################################## U S E R  H O M E ##################################################
@app.route('/userHome')
def userHome():
    print(session.get('sessionusername'))
    if session.get('sessionusername'):
        return render_template('userHome.html')
    else:
        return render_template('error.html', error = 'Unauthorized Access')


############################################## L O G O U T #######################################################
@app.route('/logout')
def logout():
    session.pop('sessionusername', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)