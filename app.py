from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
  
app = Flask(__name__)
  
  
app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'adopters'
  
mysql = MySQL(app)
  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/otherpets')
def otherpets():
    return render_template('otherpets.html')

@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('user.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)
  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))
  
@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'age' in request.form and 'email' in request.form and 'phone' in request.form and 'password' in request.form :
        userName = request.form['name']
        age = request.form['age']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s, % s, % s)', (userName, age, email, phone, password ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

@app.route('/adopt', methods=['GET', 'POST'])
def adopt():
    message = ''
    if request.method == 'POST' and 'adoptee_name' in request.form and 'adoptee_age' in request.form and 'adoptee_address' in request.form and 'adoptee_pno' in request.form and 'adoptee_email' in request.form and 'adoptee_pets_count' in request.form and 'adoptee_pet_breed' in request.form and 'adoptee_pet_adopt' in request.form:
        adoptee_name = request.form['adoptee_name']
        adoptee_age = request.form['adoptee_age']
        adoptee_address= request.form['adoptee_address']
        adoptee_pno = request.form['adoptee_pno']
        adoptee_email = request.form['adoptee_email']
        adoptee_pets_count = request.form['adoptee_pets_count']
        adoptee_pet_breed = request.form['adoptee_pet_breed']
        adoptee_pet_adopt = request.form['adoptee_pet_adopt']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM adoptions WHERE adoptee_email = %s', (adoptee_email,))
        adoption = cursor.fetchone()
        
        if adoption:
            message = 'Adoption request already exists for this email!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', adoptee_email):
            message = 'Invalid email address!'
        elif not adoptee_pet_adopt or not adoptee_name or not adoptee_age or not adoptee_pno or not adoptee_address :
            message = 'Please fill out all the fields!'
        else:
            cursor.execute('INSERT INTO adoptions (adoptee_name, adoptee_age,adoptee_address, adoptee_pno, adoptee_email,adoptee_pets_count, adoptee_pet_breed, adoptee_pet_adopt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                           (adoptee_name, adoptee_age,adoptee_address, adoptee_pno, adoptee_email,adoptee_pets_count, adoptee_pet_breed, adoptee_pet_adopt))
            mysql.connection.commit()
            message = 'Adoption request successfully submitted!'
    elif request.method == 'POST':
        message = 'Please fill out all the fields!'

    return render_template('adopt.html', message=message)

    
if __name__ == "__main__":
    app.run()