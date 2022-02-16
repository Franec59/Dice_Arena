import os
from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS, cross_origin

# mongoDB ============================================================

MONGO_HOST=os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT=os.environ.get("MONGO_PORT", "27017")
DEBUG_MODE=os.environ.get("DEBUG_MODE", "True")
SERVER_PORT=os.environ.get("SERVER_PORT", "80")
SERVER_HOST=os.environ.get("SERVER_HOST", "0.0.0.0")

app = Flask("parties")
CORS(app)

client = MongoClient(host=MONGO_HOST, port=int(MONGO_PORT))
db = client["parties"]
collection = db["parties"]

# POST request : Pseudo / nom de la partie =============================================
@app.post("/partie")
@cross_origin()
def sauvegarder_Partie():
    parties = request.json
    collection.insert_one(parties)
    parties["_id"] = str(parties["_id"])
    return parties


# delete by id request ===================================================
@app.delete("/partie/<id>")
@cross_origin()
def supprimer_pseudo(id:str):
    try:
        objectId = ObjectId(id)
    except:
        return Response(response="l'id doit correspondre a un ObjectId", status=400)
    result = collection.delete_one({"_id":objectId})
    if result.deleted_count:
        return Response(status=202)
    else:
        return Response(status=404)

# delete partie + tous les joueurs =================================================================
@app.delete("/deletepartie/<id>")
def supprimer_partie(id:str):
    objectId = ObjectId(id)
    deleted_doc = collection.find_one_and_delete({"_id":objectId})
    joueurs = { "numero_partie": id }
    collection.delete_many(joueurs)

    return ("Partie supprimée :", deleted_doc)


# # GET request joueurs + nom de la partie ======================================================
# @app.get("/partie")
# @cross_origin()
# def retourner_joueurs():
#     joueurs_list = []
#     for data in collection.find():
#         data["_id"] = str(data["_id"])
#         joueurs_list.append(data)
#     return jsonify(joueurs_list)

# requête pour récupérer le joueur en cours ===================================
@app.get("/joueur/<id>")
def get_joueur(id:str):
    try:
        objectId = ObjectId(id)
    except:
        return Response(response="l'id doit correspondre à un ObjectId", status=400)
    joueur = collection.find_one({"_id":ObjectId(id)})
    if joueur:
        joueur["_id"] = str(joueur["_id"])    
        return joueur
    else:
        return Response(status=404)
    
# requête pour aller la partie en cours ===================================
@app.get("/mapartie/<id>")
def get_maPartie(id:str):
    try:
        objectId = ObjectId(id)
    except:
        return Response(response="l'id doit correspondre à un ObjectId", status=400)
    maPartie = collection.find_one({"_id":ObjectId(id)})
    if maPartie:
        maPartie["_id"] = str(maPartie["_id"])    
        return maPartie
    else:
        return Response(status=404)

# GET request pour la liste des joueurs de la partie ======================================================
@app.get("/liste/<idpartie>")
@cross_origin()
def liste_joueurs(idpartie:str):
    joueurs_list = []
    for data in collection.find({ "numero_partie": idpartie }):
        data["_id"] = str(data["_id"])
        joueurs_list.append(data)
    return jsonify(joueurs_list)


if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=int(SERVER_PORT), debug=bool(DEBUG_MODE))