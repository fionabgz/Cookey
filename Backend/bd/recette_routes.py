from flask import Blueprint,jsonify,request
from pymongo import MongoClient
from bson.json_util import dumps
import json
from bson import ObjectId
from flask import request


con= MongoClient("mongodb://localhost:27017")
db = con['SaeDB']


recette_bp = Blueprint('recette', __name__)

id_incr = db.recette.count_documents({})

#test route
@recette_bp.route('/h')
def hello_world():
	return 'Hefdslldo, f!!'


@recette_bp.route('/liste_recettes', methods=['GET'])
def afficher_recettes():
    recettes = list(db.recette.find({}))
    if recettes:
        return jsonify(recettes), 200
    else:
        return jsonify({'message': 'Aucune recette trouvée'}), 404


@recette_bp.route('/afficher/<int:idRecette>', methods=['GET'])
def afficher_recette_id(idRecette):
    recette = db.recette.find_one({"_id": idRecette})
    
    if recette:
        return jsonify(recette), 200
    else:
        return jsonify({'error': f"ID {idRecette} non trouvée dans la base de données"}), 404



@recette_bp.route('/recettes_possibles', methods=['POST'])
def afficher_recettes_possibles():
    try:
        ingredients_input = request.get_json().get('ingredients')
                
        recettes_possibles = list(db.recette.find({}))
        
        recettes_filtrees = []
        for recette in recettes_possibles:

            ingredients_recette = [ingredient['nom'] for ingredient in recette['ingredients']]
            if set(ingredients_input).issubset(set(ingredients_recette)):
                recettes_filtrees.append(recette)
        
        return jsonify(recettes_filtrees), 200
    except Exception as e:
        print(f"error: {e}")
        return jsonify({'message': 'error  request'}), 500
#gerer erreur 