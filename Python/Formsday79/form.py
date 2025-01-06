from flask import Flask, request
app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
  page =""
  form = request.form
  if form["college"] == "erc":
    page += f"You're alright {form['username']}"
  else:
    page += f"You've picked wrong, {form['username']}"  
  return page  
@app.route('/')
def index():
  page = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Forms</title>
    </head>
    <body>
      <form method="post" action="/process">
        <p>Name: <input type="text" placeholder="user name" name="username" required></p>
        <p>Email: <input type="email" placeholder="thor@email.com" name="email" required></p>
        <input type="hidden" name="userID" value="123">
        <p>College: <select name="college">
          <option value="erc">erc</option>
          <option value="wrc">wrc</option>
          <option value="pulchowk">pulchowk</option>
        </select>
        </p>
        <button type="submit">Save data</button>
        
      </form>
    </body>
    </html>"""
  return page

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5005, debug=True)