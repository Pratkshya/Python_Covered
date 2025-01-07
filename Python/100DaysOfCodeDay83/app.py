from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return "Hello from flask"

@app.route("/blog/hello")  
def hr():
  return redirect("/hello")

@app.route("/blog/bye")  
def br():
  return redirect("/bye")

@app.route('/hello', methods = ['GET'])
def hello():
  data = request.args
  template = "default"
  if data != {}:
    template = data["template"]
  title = "Hello World"
  date = "January 7"
  message = "Here is first blog entry!"
  return render_template('index.html', title=title, date=date, message=message, template=template)

@app.route('/bye', methods = ['GET'])
def bye():
  data = request.args
  template = "default"
  if data != {}:
    template = data["template"]
  title = "Bye World"
  date = "January 8"
  message = "Here is last blog entry!"
  return render_template('index.html', title=title, date=date, message=message, template=template)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5007, debug=True)