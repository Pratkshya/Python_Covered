from flask import Flask, request
app = Flask(__name__)

logins = {}

logins["pratkshya"] = {"email": "p@p.com", "password": "cat"}
logins["sita"] = {"email": "s@s.com", "password": "dog"}
logins["anusha"] = {"email": "a@a.com", "password": "yuby"}

@app.route("/login", methods = ["POST"])
def login():
  form = request.form
  isThere = False
  details = {}
  try:
    details = logins[form["username"]]
    isThere = True
  except:
    return "Username, email or password is incorrect"
  
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "You are logged in."
  else:
    return "Username, email or password is incorrect."
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
      <form method="post" action="/login">
        <p>Username: <input type="text" name="username" required></p>
        <p>Email: <input type="Email" name="email" required></p>
        <p>Password: <input type="password" name="password" required></p>
        <button type="submit">Login</button>
      </form>
    </body>
    </html>"""
  return page

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5007, debug=True)
