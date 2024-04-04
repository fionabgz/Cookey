from flask import Blueprint,jsonify,request
from pymongo import MongoClient
import json


con= MongoClient("mongodb://localhost:27017")
db=con.SaeDB


personne_bp = Blueprint('personne', __name__)


@personne_bp.route('/<string:personne_nom>',methods=['GET'])
def get_personne(personne_nom):
	return db.personne.find_one({"nom": personne_nom},{"_id":0,"nom":1,"ingredient":1,"liste_course":1})



@personne_bp.route('/<string:personne_nom>/ajouter',methods=['PUT'])
def ajouter_ingredient(personne_nom):
	data = request.get_json()
	ingredient = data.get('ingredient')
	db.personne.update_one({"nom":personne_nom},{"$push":{"liste_course":ingredient}})
	return jsonify({'message': 'maj succès'})


@personne_bp.route('/<string:personne_nom>/vider',methods=['DELETE'])
def vider_liste_course(personne_nom):
	db.personne.update_one({"nom":personne_nom},{"$set":{"liste_course":[]}})
	return jsonify({'message': 'maj succès'})

