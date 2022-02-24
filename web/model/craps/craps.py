import os
from flask import Flask, jsonify, request, Response
from system_craps import Craps
from flask_cors import CORS, cross_origin

# mongoDB ============================================================

DEBUG_MODE=os.environ.get("DEBUG_MODE", "True")
SERVER_PORT=os.environ.get("SERVER_PORT", "90")
SERVER_HOST=os.environ.get("SERVER_HOST", "0.0.0.0")

app=Flask(__name__)
CORS(app)

@app.get("/run")
def run_craps():
    Craps.game(2)
    return "Système démarré"

@app.post("/launch")
def lancer():
    Craps.diceNumber()
    return "dice rolling"





if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=int(SERVER_PORT), debug=bool(DEBUG_MODE))