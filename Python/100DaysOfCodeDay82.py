from flask import Flask, request
app = Flask(__name__)

@app.route('/language', methods=["GET"])
def lang():
  get = request.args
  if get == {}:
    return "Nothing here"
  if get["lang"] == "eng":
    return "Hello, and welcome to my website."
  elif get["lang"] == "nep":
    return "नमस्ते, र मेरो वेबसाइटमा स्वागत छ।"

@app.route('/')
def index():
  return "Hello from flask"
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5009, debug=True)