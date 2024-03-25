# models/tournoi_model.py
from bson import ObjectId
from database import db

tournoi_collection = db.tournoi

def ajouter_tournoi(tournoi):
    return tournoi_collection.insert_one(tournoi).inserted_id

def obtenir_tournois():
    return list(tournoi_collection.find())

def obtenir_tournoi_par_id(id):
    return tournoi_collection.find_one({'_id': ObjectId(id)})

def mettre_a_jour_tournoi(id, tournoi):
    return tournoi_collection.update_one({'_id': ObjectId(id)}, {'$set': tournoi})

def supprimer_tournoi(id):
    return tournoi_collection.delete_one({'_id': ObjectId(id)})

def ajouter_match_tournoi(tournoi_id, match):
    return tournoi_collection.update_one({'_id': ObjectId(tournoi_id)}, {'$push': {'Matchs': match}})
