# routes/tournoi_routes.py
from flask import Blueprint, request, jsonify
from models.tournoi_model import ajouter_tournoi, obtenir_tournois, obtenir_tournoi_par_id, mettre_a_jour_tournoi, supprimer_tournoi, ajouter_match_tournoi
from bson import ObjectId

tournoi_bp = Blueprint('tournoi_bp', __name__)

@tournoi_bp.route('/', methods=['POST'])
def ajouter():
    tournoi_id = ajouter_tournoi(request.json)
    return jsonify({'resultat': 'Tournoi ajouté avec succès', 'id': str(tournoi_id)})

@tournoi_bp.route('/', methods=['GET'])
def obtenir_tous():
    tournois = obtenir_tournois()
    for tournoi in tournois:
        tournoi['_id'] = {"$oid": str(tournoi['_id'])}
    return jsonify(tournois)

@tournoi_bp.route('/<id>', methods=['GET'])
def obtenir(id):
    tournoi = obtenir_tournoi_par_id(id)
    if tournoi:
        tournoi['_id'] = {"$oid": str(tournoi['_id'])}
        return jsonify(tournoi)
    return jsonify({'erreur': 'Tournoi non trouvé'}), 404

@tournoi_bp.route('/<id>', methods=['PUT'])
def mettre_a_jour(id):
    resultat = mettre_a_jour_tournoi(id, request.json)
    if resultat.matched_count:
        return jsonify({'resultat': 'Tournoi mis à jour avec succès'})
    return jsonify({'erreur': 'Mise à jour échouée ou tournoi non trouvé'}), 404

@tournoi_bp.route('/<id>', methods=['DELETE'])
def supprimer(id):
    resultat = supprimer_tournoi(id)
    if resultat.deleted_count:
        return jsonify({'resultat': 'Tournoi supprimé avec succès'})
    return jsonify({'erreur': 'Suppression échouée ou tournoi non trouvé'}), 404

@tournoi_bp.route('/<tournoi_id>/match', methods=['POST'])
def ajouter_match_tournoi(tournoi_id):
    match = request.json
    resultat = ajouter_match_tournoi(tournoi_id, match)
    if resultat.modified_count:
        return jsonify({'message': 'Match ajouté avec succès au tournoi'})
    else:
        return jsonify({'erreur': 'Ajout du match échoué ou tournoi non trouvé'}), 404
