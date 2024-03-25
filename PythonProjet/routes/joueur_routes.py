# routes/joueur_routes.py
from flask import Blueprint, request, jsonify
from models.joueur_model import ajouter_joueur, obtenir_joueurs, obtenir_joueur_par_id, mettre_a_jour_joueur, supprimer_joueur
import json

joueur_bp = Blueprint('joueur_bp', __name__)

@joueur_bp.route('/', methods=['POST'])
def ajouter():
    joueur_id = ajouter_joueur(request.json)
    return jsonify({'resultat': 'Joueur ajouté avec succès', 'id': str(joueur_id)})

@joueur_bp.route('/', methods=['GET'])
def obtenir_tous():
    joueurs = obtenir_joueurs()
    joueurs_transformes = [{'_id': str(joueur['_id']), **joueur} for joueur in joueurs]
    return jsonify(joueurs_transformes)

@joueur_bp.route('/<id>', methods=['GET'])
def obtenir(id):
    joueur = obtenir_joueur_par_id(id)
    if joueur:
        joueur['_id'] = str(joueur['_id'])
        return jsonify(joueur)
    return jsonify({'erreur': 'Joueur non trouvé'}), 404

@joueur_bp.route('/<id>', methods=['PUT'])
def mettre_a_jour(id):
    resultat = mettre_a_jour_joueur(id, request.json)
    if resultat.matched_count:
        return jsonify({'resultat': 'Joueur mis à jour avec succès'})
    return jsonify({'erreur': 'Mise à jour échouée ou joueur non trouvé'}), 404

@joueur_bp.route('/<id>', methods=['DELETE'])
def supprimer(id):
    resultat = supprimer_joueur(id)
    if resultat.deleted_count:
        return jsonify({'resultat': 'Joueur supprimé avec succès'})
    return jsonify({'erreur': 'Suppression échouée ou joueur non trouvé'}), 404
