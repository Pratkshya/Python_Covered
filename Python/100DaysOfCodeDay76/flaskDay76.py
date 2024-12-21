from flask import Flask
import datetime

app = Flask(__name__, static_url_path = "/static")

@app.route('/')
def index():
  home = f"""<html>
  <body>
  <p><a href="/home">Go to home page</a></p>
  <p><a href="/portfolio">Go to portfolio page</a></p>  
  </body>
  </html>"""
  return home

@app.route('/portfolio')  
def myPortfolio():
  page2 = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My social media handles</title>
  <link rel="stylesheet" href="/static/portfolio.css">
</head>
<body>
  <div>
    <img src="/static/image/p.jpg" alt="Profile picture">
    <h1>Pratikshya Parajuli</h1>
    <h5>The prettiest nerd you've ever seen</h5>
    <h3>Socials</h3>
    <ul>
      <li>Facebook: <a href="https://www.facebook.com/pratikshya.parajuli.56" target="_blank">(@Pratikshya Parajuli)</a></li>
      <li>Instagram: <a href="https://www.instagram.com/pra_tikshya_/" target="_blank">(@pra_tikshya_)</a></li>
      <li>Github: <a href="https://github.com/Pratkshya" target="_blank">(@Pratkshya)</a></li>
      <li>Linkedln: <a href="https://www.linkedin.com/in/pratikshya-parajuli-25714b293/" target="_blank">(@Pratkshya)</a></li>
    </ul>
  </div>
</body>
</html>"""
  return page2

@app.route('/home')  
def homePage():
  today = datetime.date.today()
  page = f""" <!DOCTYPE html>
 <html lang="en">
 <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pratkshya's Portfolio</title>
  <link rel="stylesheet" href="/static/homePage.css">
 </head>
 <body>
   <h1>Pratkshya's Portfolio</h1>
   <h2 id="date">Current date: {today}</h2>
   <h2>Day 74 Project</h2>
   <p>On day 74 of Python programming, I've created my own portfolio using HTML and CSS concepts. It demonstrates the abstract knowledge on how a webpage is given a life to its own through styling and designing.<br> Click the image below to view "Day 74: 100 Days of Code:"</p>
   <a href="https://www.youtube.com/watch?v=sHxTcIe-AOM&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=125" target="_blank"><img src="/static/image/Screenshot 2024-12-20 214300.png" ></a>
 </body>
 </html>"""
  return page

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True)