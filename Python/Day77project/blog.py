from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from flask"

@app.route('/firstPage')
def firstPage():
    title = "Hello World"
    date = "October 25th"
    text = "Here is my first blog entry."
    return render_template("index1.html", title=title, date=date, text=text)

@app.route('/endPage')
def endPage():
    title = "Bye World"
    date = "October 25th"
    text = "Here is my first blog entry."
    return render_template("index2.html", lastTitle=title, ldate=date, ltext=text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)
