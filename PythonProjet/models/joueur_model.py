# models/joueur_model.py
from bson import ObjectId
from database import db

joueur_collection = db.joueur
def ajouter_joueur(joueur_data):
    try:
        # Assurez-vous que joueur_data est un dictionnaire
        if isinstance(joueur_data, dict):
            joueur_id = joueur_collection.insert_one(joueur_data).inserted_id
            return joueur_id
        else:
            raise TypeError("Le document doit être un dictionnaire Python")
    except Exception as e:
        print("Erreur lors de l'insertion du joueur :", e)
        raise

def obtenir_joueurs():
    joueurs = list(joueur_collection.find())
    for joueur in joueurs:
        joueur['_id'] = {"$oid": str(joueur['_id'])} 
    return joueurs

def obtenir_joueur_par_id(id):
    joueur = joueur_collection.find_one({'_id': ObjectId(id)})
    if joueur:
        joueur['_id'] = {"$oid": str(joueur['_id'])}  
    return joueur

def mettre_a_jour_joueur(id, joueur):
    return joueur_collection.update_one({'_id': ObjectId(id)}, {'$set': joueur})

def supprimer_joueur(id):
    return joueur_collection.delete_one({'_id': ObjectId(id)})
