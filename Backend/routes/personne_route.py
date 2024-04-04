from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

con = MongoClient("mongodb://localhost:27017")
db = con.SaeDB
bcrypt = Bcrypt()

personne_bp = Blueprint('personne', __name__)



#test route
@personne_bp.route('/h')
def hello_world():
	return 'Hefdslldo, f!!'


@personne_bp.route('/<string:personne_nom>',methods=['GET'])
def get_personne(personne_nom):
	return db.personne.find_one({"nom": personne_nom},{"_id":0,"nom":1,"ingredient":1,"liste_course":1})



@personne_bp.route('/<string:personne_nom>/course/ajouter',methods=['PUT'])
def ajouter_ingredient(personne_nom):
	data = request.get_json()
	ingredient = data.get('ingredient')
	db.personne.update_one({"nom":personne_nom},{"$push":{"liste_course":ingredient}})
	return jsonify({'message': 'maj succès'})


@personne_bp.route('/<string:personne_nom>/course/vider',methods=['DELETE'])
def vider_liste_course(personne_nom):
	db.personne.update_one({"nom":personne_nom},{"$set":{"liste_course":[]}})
	return jsonify({'message': 'maj succès'})

@personne_bp.route('/inscription', methods=['POST'])
def register():
    data = request.get_json()
    username =data.get('username')
    password = data.get('password')
    nom = data.get('nom')
    listeIngredients = []
    listeCourse = []

    if db.personne.find_one({'username': username}):
        return jsonify({'message': 'usermanme pris'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    personne_data = {
        'username': username,
        'password': hashed_password,
        'nom': nom,
        'listeIngredients': listeIngredients,
        'listeCourse': listeCourse
    }
    db.personne.insert_one(personne_data)

    return jsonify({'message': 'inscription reussie'}), 201

@personne_bp.route('/connexion', methods=['POST'])
def connexion():
    data = request.get_json()
    username =data.get('username')
    password = data.get('password')

    user = db.personne.find_one({'username': username})

    if user and bcrypt.check_password_hash(user['password'], password):
        return jsonify({'message': 'connecté'}), 200
    else:
        return jsonify({'message': 'incorrect'}), 401



@personne_bp.route('/<string:personne_nom>/frigo/ajouter',methods=['PUT'])
def ajouter_ingredient_frigo(personne_nom):
	data = request.get_json()
	ingredient = data.get('ingredient')
	db.personne.update_one({"nom":personne_nom},{"$push":{"frigo":{"ingredient":ingredient}}})
	return jsonify({'message': 'maj succès'})

 

@personne_bp.route('/<string:personne_nom>/frigo/retirer',methods=['PUT'])
def retirer_ingredient_frigo(personne_nom):
	data = request.get_json()
	ingredient = data.get('ingredient')
	print(ingredient)
	db.personne.update_one({"nom":personne_nom},{'$pull':{"frigo":{"ingredient":ingredient}}})
	print(afficher_frigo(personne_nom))
	return jsonify({'message': 'maj succès'})

 

 

@personne_bp.route('/<string:personne_nom>/frigo/afficher',methods=['GET'])

def afficher_frigo(personne_nom):
	personne = db.personne.find_one({"nom":personne_nom},{"_id":0, "nom":1, "frigo":1})
	return personne['frigo']

 

@personne_bp.route('/<string:personne_nom>/course/afficher',methods=['GET'])

def afficher_course(personne_nom):
	personne = db.personne.find_one({'nom':personne_nom},{'_id':0,'nom':1, 'liste_course':1})
	return personne['liste_course']

 

 