from flask import Flask, render_template, request, abort
from werkzeug.utils import redirect

# Objet pour stocker flask
app = Flask(__name__)

# Méthode => route

@app.route("/")
def index():
    online_users = mongo.db.users.find({"online": True})
    return render_template(index.html,  online_users=online_users)

@app.route()