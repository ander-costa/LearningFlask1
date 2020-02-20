from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return render_template("index.html", title = "Olá Flask", message = "Olá, Flask!", content = " on " + formatted_now)