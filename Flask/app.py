from flask import Flask, render_template, request, redirect
from db import Database

dbo = Database()

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('login.html')


@app.route('/register')
def registration(): 
    return render_template('register.html')


@app.route('/register-data', methods=['post'])
def registration_data(): 
    user_name = request.form.get('name')
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    response = dbo.insert(user_name, user_email, user_password)

    if response:  
        return render_template("login.html", message="Registration Successful. Kindly login to proceed.")
    else: 
        return render_template("register.html", message="Email already Exists!")


@app.route('/perform-login', methods=['post'])
def perform_login(): 
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    response = dbo.search(user_email, user_password)

    if response: 
        return redirect('/profile')
    else: 
        return render_template('login.html', message="Incorrect email/password")
    

@app.route('/profile')
def profile(): 
    return render_template('/profile.html')


@app.route('/ner')
def ner(): 
    return render_template('ner.html')


@app.route('/perform-ner', methods=['post'])
def perform_ner(): 
    text = request.form.get('ner_text')

@app.route('/sentiment-analysis')
def sentiment_analysis():
    return 'sentiment analysis'


@app.route('/abuse-detection')
def abuse_detection(): 
    return 'abuse detection'


app.run(debug=True)