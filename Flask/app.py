from flask import Flask, render_template, request

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

    return f'Name: {user_name} Email: {user_email} Password: {user_password}'


app.run(debug=True)