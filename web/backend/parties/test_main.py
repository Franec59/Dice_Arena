# test des fonctions de main.py avec pytest

# pour installer pytest : pip install -U pytest
# pour lancer pytest : taper la commande pytest

# tester pytest ====================================================
def inc(x):
    return x + 1

def test_anwser():
    assert inc(3) == 5


# # test d'une insertion de données dans la BDD =============================================

# import os
# from readline import insert_text
# from flask import Flask, jsonify, request, Response
# from pymongo import MongoClient
# from bson import ObjectId

# # mongoDB ============================================================

# MONGO_HOST=os.environ.get("MONGO_HOST", "localhost")
# MONGO_PORT=os.environ.get("MONGO_PORT", "27017")
# DEBUG_MODE=os.environ.get("DEBUG_MODE", "True")
# SERVER_PORT=os.environ.get("SERVER_PORT", "80")
# SERVER_HOST=os.environ.get("SERVER_HOST", "0.0.0.0")

# app = Flask("parties")

# client = MongoClient(host=MONGO_HOST, port=int(MONGO_PORT))
# db = client["parties"]
# collection = db["parties"]

# def test():
#     test_insert = { "test" : "test"}
#     collection.insert_one(test_insert)
#     test_insert["_id"] = str(test_insert["_id"])
#     result= collection.find_one({ "test": "test" })
#     assert result == test_insert


# if __name__ == "__main__":
#     app.run(host=SERVER_HOST, port=int(SERVER_PORT), debug=bool(DEBUG_MODE))

