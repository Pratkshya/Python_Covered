from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/robot", methods = ["POST"])
def robot():
  form = request.form
  if form['yesno'] == "Yes":
    return "You are a robot!"
  elif "error" in form['text'].lower():
    return "You are a robot!"
  elif form['food'] == "synthetic oil":
    return "You are a robot!"
  else:
    return "Hello there fellow human"

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5008, debug=True)