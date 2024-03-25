# routes/equipe_routes.py
from flask import Blueprint, request, jsonify
from models.equipe_model import (ajouter_equipe, obtenir_equipes, obtenir_equipe_par_id, 
mettre_a_jour_equipe, supprimer_equipe, ajouter_joueur_equipe, retirer_joueur_equipe)
from bson import ObjectId

equipe_bp = Blueprint('equipe_bp', __name__)

@equipe_bp.route('/', methods=['POST'])
def ajouter():
    equipe_id = ajouter_equipe(request.json)
    return jsonify({'resultat': 'Équipe ajoutée avec succès', 'id': str(equipe_id)})

@equipe_bp.route('/', methods=['GET'])
def obtenir_tous():
    equipes = obtenir_equipes()
    for equipe in equipes:
        equipe['_id'] = str(equipe['_id'])
    return jsonify(equipes)

@equipe_bp.route('/<id>', methods=['GET'])
def obtenir(id):
    equipe = obtenir_equipe_par_id(ObjectId(id))
    if equipe:
        equipe['_id'] = str(equipe['_id'])
        return jsonify(equipe)
    return jsonify({'erreur': 'Équipe non trouvée'}), 404

@equipe_bp.route('/<id>', methods=['PUT'])
def mettre_a_jour(id):
    resultat = mettre_a_jour_equipe(ObjectId(id), request.json)
    if resultat.matched_count:
        return jsonify({'resultat': 'Équipe mise à jour avec succès'})
    return jsonify({'erreur': 'Mise à jour échouée ou équipe non trouvée'}), 404

@equipe_bp.route('/<id>', methods=['DELETE'])
def supprimer(id):
    resultat = supprimer_equipe(ObjectId(id))
    if resultat.deleted_count:
        return jsonify({'resultat': 'Équipe supprimée avec succès'})
    return jsonify({'erreur': 'Suppression échouée ou équipe non trouvée'}), 404

@equipe_bp.route('/<equipe_id>/ajouter_joueur/<joueur_id>', methods=['PUT'])
def ajouter_joueur(equipe_id, joueur_id):
    resultat = ajouter_joueur_equipe(ObjectId(equipe_id), joueur_id)
    if resultat.modified_count:
        return jsonify({'resultat': 'Joueur ajouté à l\'équipe avec succès'})
    return jsonify({'erreur': 'Ajout du joueur à l\'équipe échoué ou équipe non trouvée'}), 404

@equipe_bp.route('/<equipe_id>/retirer_joueur/<joueur_id>', methods=['PUT'])
def retirer_joueur(equipe_id, joueur_id):
    resultat = retirer_joueur_equipe(ObjectId(equipe_id), joueur_id)
    if resultat.modified_count:
        return jsonify({'resultat': 'Joueur retiré de l\'équipe avec succès'})
    return jsonify({'erreur': 'Retrait du joueur de l\'équipe échoué ou équipe non trouvée'}), 404
