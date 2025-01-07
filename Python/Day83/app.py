from flask import Flask, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
app = Flask(__name__)

#database to store users input
def get_db_connection():
  conn= mysql.connector.connect(
    host='localhost',
    user='root',
    password='#qW2ftfn=,F4fs.-',
    database='user_db'
  )
  return conn

@app.route('/register', methods=['GET','POST'])
def register():
  if request.method == "POST":
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    hashed_password = generate_password_hash(password)

    #save to MySQL database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
      cursor.execute(
        "INSERT INTO USERS (username, name, password) VALUES (%s, %s, %s)",
        (username, name, hashed_password)
      )
      conn.commit()
      return redirect(url_for('login'))
    except mysql.connector.Error as err:
      return f"Error: {err}"
    finally:
      cursor.close()
      conn.close()
  return render_template('registration.html')

@app.route('/login', methods=['POST', 'GET'])  
def login():
  if request.method == 'POST':
    #get data from the register page
    username = request.form['username']
    password = request.form['password']
    
    #to retrieve from MySQL database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM USERS WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if user:
      if check_password_hash(user['password'], password):
        return redirect(url_for('welcome', username=username))
      else:
        return "Incorrect password"  
    else:
      return "Username not found"   
  return render_template('login.html')

@app.route('/welcome/<username>')
def welcome(username):
  return f"User {username}, loggedin successfully!"
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5008, debug=True)