from flask import Flask, request, url_for, session, render_templates

app = Flask(__name__)

@app.route("/")
def blog():
    return render_templates("blog.html")

if __name__ == '__main__':
    app.run(debug=True)