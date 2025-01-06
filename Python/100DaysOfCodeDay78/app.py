from flask import Flask, render_template
app = Flask(__name__)

myReflections = {}

myReflections["13"] = {"link": "https://replit.com/@pratikshyaparaj/100-Days-Of-Coding-Day-13",
                       "message": "Was a bit of a head scratcher, but I got there in the end. Even if I was a bit lazy with the css😭"}

myReflections["14"] = {"link": "https://replit.com/@pratikshyaparaj/100-Days-Of-Coding-Day-14",
                       "message": "It was more simpler than I thought🥲"}

@app.route("/")
def welcomePage():
  return "Hello from Flask"

@app.route("/<pageNumber>")
def index(pageNumber):
  global myReflections
  if pageNumber in myReflections:
    return render_template("index.html", day=pageNumber, link=myReflections[pageNumber]["link"],reflection=myReflections[pageNumber]["message"])
  else:
    return "Reflection not found", 404
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5005, debug=True)