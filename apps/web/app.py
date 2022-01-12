from flask import Flask, render_template, request
from werkzeug.utils import redirect

# Objet pour stocker flask
app = Flask(__name__)

# Méthode => route

@app.route("/")
def index():
    return render_template(index.html)
      
