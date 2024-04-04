from flask import Blueprint,jsonify,request
from pymongo import MongoClient
import json


con= MongoClient("mongodb://localhost:27017")
db=con.SaeDB
#db = con['SaeDB']


recette_bp = Blueprint('recette', __name__)

#test route
@recette_bp.route('/h')
def welcome():
	return 'hello welcome in recipe!!'

@recette_bp.route('all',methods=['GET'])
def get_all_recette():
	recette = list(db.recette.find({},{"_id":0,"nom":1}))
	return jsonify(recette), 200

@recette_bp.route('/all/time', methods=['GET'])
def get_recettes_time():
    recettes = list(db.recette.find({}).sort("temps", 1))
    if recettes:
        return jsonify(recettes), 200
    else:
        return jsonify({'message': 'Aucune recette trouvée'}), 404

@recette_bp.route('/<string:recette_nom>',methods=['GET'])
def get_recette(recette_nom):
	return db.recette.find_one({"nom": recette_nom},{"_id":0,"nom":1,"instruction":1})


@recette_bp.route('nutriscore/<string:nutriscore>',methods=['GET'])
def get_recette_par_nutriscore(nutriscore):
	recette = list(db.recette.find({"nutriscore":nutriscore},{"_id":0,"nom":1}))
	return jsonify(recette), 200


@recette_bp.route('/<string:nom>/<int:nb_personne>',methods=['GET'])
def get_recette_par_nb_personne(nom,nb_personne):
	recette= db.recette.find_one({"nom": nom},{"_id":0,"nom":1,"instruction":1,"ingredient":1,"nutriscore":1,"temps":1,"nbPersonne":1})
	print(recette)
	ingredient=recette['ingredient']
	for i in ingredient:
		print(i["nb"])
		i["nb"]= i["nb"]*nb_personne/recette["nbPersonne"]
		print(i["nb"])
	recette["ingredient"]=ingredient
	return recette


#visu pour debug
@recette_bp.route('/liste_recettes', methods=['GET'])
def get_recettes():
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



