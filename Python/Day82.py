from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods = ["GET"])
def index():
  get = request.args
  if get["name"].lower() == "pratkshya":
    return "Hello bhai"
  return "No data"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5009, debug=True)