from flask import Flask
app = Flask(__name__)

@app.route('/<pageNumber>')
def index(pageNumber):
  return f"This is page {pageNumber}"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5004, debug = True)