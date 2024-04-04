from flask import Blueprint,jsonify,request
from pymongo import MongoClient
import json


con= MongoClient("mongodb://localhost:27017")
db=con.SaeDB


recette_bp = Blueprint('recette', __name__)


@recette_bp.route('/<string:recette_nom>',methods=['GET'])
def get_recette(recette_nom):
	return db.recette.find_one({"nom": recette_nom},{"_id":0,"nom":1,"instruction":1})

@recette_bp.route('all',methods=['GET'])
def get_all_recette():
	recette = list(db.recette.find({},{"_id":0,"nom":1}))
	return jsonify(recette), 200


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



