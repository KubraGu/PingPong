# models/equipe_model.py
from database import db
from bson import ObjectId

equipe_collection = db.equipe

def ajouter_equipe(equipe):
    return equipe_collection.insert_one(equipe).inserted_id

def obtenir_equipes():
    return list(equipe_collection.find())

def obtenir_equipe_par_id(id):
    return equipe_collection.find_one({'_id': ObjectId(id)})

def mettre_a_jour_equipe(id, updates):
    return equipe_collection.update_one({'_id': ObjectId(id)}, {'$set': updates})

def supprimer_equipe(id):
    return equipe_collection.delete_one({'_id': ObjectId(id)})

def ajouter_joueur_equipe(equipe_id, joueur_id):
    return equipe_collection.update_one({'_id': ObjectId(equipe_id)}, {'$addToSet': {'Joueurs': {'$oid': joueur_id}}})

def retirer_joueur_equipe(equipe_id, joueur_id):
    return equipe_collection.update_one({'_id': ObjectId(equipe_id)}, {'$pull': {'Joueurs': {'$oid': joueur_id}}})
