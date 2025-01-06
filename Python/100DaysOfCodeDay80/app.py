from flask import Flask, request
app = Flask(__name__)

count = 0
@app.route("/process", methods = ['POST'])
def process():
  global count
  page = ""
  username = request.form.get("username", "").strip()
  email = request.form.get("email", "").strip()
  password = request.form.get("password", "").strip()

  if username and email and password:
    count += 1
    if count <= 3:
      page = f"Welcome {username}! You are successfully loged in.<br>"
    else:
      page = "Maximus login limit reached. No more logins allowed.<br>"   
  else:
    page = "Error: Username, email or password is incorrect. Try again.<br>"  
  return page
@app.route('/')
def index():
  page = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>LogIn Page</title>
    </head>
    <body>
      <form method="post" action="/process">
        <p>Username: <input type="text" name="username" required></p>
        <p>Email: <input type="Email" name="email" required></p>
        <p>Password: <input type="password" name="password" required></p>
        <button type="submit">Login</button>
      </form>
    </body>
    </html>"""
  return page
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5006, debug = True)