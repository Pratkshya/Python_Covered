from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)

#sets the secret key to use sessions
app.secret_key = "thisisencrypted@12"

#Initialize database
def initialize_db():
  conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '#qW2ftfn=,F4fs.-',
    database = 'user_db'
  )
  return conn  

#Welcome page route
@app.route('/')
def index():
  return render_template('welcome.html')

#Home page route
@app.route('/index.html')
def homePage():
  return render_template('index.html')

#Signup page route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  session.pop('username', None)

  if request.method == 'POST':
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    hashed_password = generate_password_hash(password)

    #connect to database
    conn = initialize_db()
    #create a cursor object to interact with database
    cursor = conn.cursor()
    
    try:

      cursor.execute("SELECT username FROM USERS WHERE username = %s", (username,))
      existing_user = cursor.fetchone()

      if existing_user:
        return "Error: Username already exists. Please, choose a different username!"
      #adds data to the database
      cursor.execute(
        # INSERT is a sql query which tells db to add new record with the given values
        "INSERT INTO USERS (username, name, password) VALUES (%s, %s,%s)", (username, name, hashed_password)) # VALUES acts as a tuple containing the actual data to insert in a specific order. 
      conn.commit()
      return redirect(url_for('login'))
    
    #error handling
    except mysql.connector.Error as err:
      return f"Error: {err}"
    
    #to always close the connection even when the try..expect fails
    finally:
      cursor.close()
      conn.close()
  return render_template('signup.html')   

#Login page route
@app.route('/login', methods=['POST', 'GET'])
def login():
  if 'username' in session:
    return redirect(url_for('hello', username=session['username']))

  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    conn = initialize_db()
    cursor = conn.cursor(dictionary=True) #to work  with query results

    cursor.execute("SELECT * FROM USERS WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if user:
      if check_password_hash(user['password'], password):
          # Store username in session after login
          session['username'] = username
          return redirect(url_for('hello', username=username))
      else:
          return "Incorrect password."
    else:
      return "Username not found."

  return render_template('login.html')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/index.html')

@app.route('/hello/<username>')
def hello(username):
  if 'username' in session:
    page = f"""User {username}, you are logged in successfully!"
    <button type="button" onClick="location.href='/logout'">Logout</button>"""
    return page
  else:
      return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5008, debug=True)