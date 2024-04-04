from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

con = MongoClient("mongodb://localhost:27017")
db = con.SaeDB
bcrypt = Bcrypt()

personne_bp = Blueprint('personne', __name__)


#test route 
@personne_bp.route('/h')
def welcome():
	return 'hello, welcome in personne!!'

@personne_bp.route('/inscription', methods=['POST'])
def inscription():
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

@personne_bp.route('/<string:username>/supprimer', methods=['DELETE'])
def supprimer_compte(username):
    user = db.personne.find_one({'username': username})
    if user:
        db.personne.delete_one({'username': username})
        return jsonify({'message': 'Compte supprimé '}), 200
    else:
        return jsonify({'message': 'Utilisateur '}), 404


@personne_bp.route('/<string:personne_nom>',methods=['GET'])
def get_personne(personne_nom):
	return db.personne.find_one({"nom": personne_nom},{"_id":0,"nom":1,"ingredient":1,"liste_course":1})


@personne_bp.route('/<string:username>/ajouter',methods=['PUT'])
def ajouter_ingredient(username):
    data = request.get_json()
    ingredient = data.get('ingredient')
    result = db.personne.update_one({"username":username},{"$push":{"liste_course":ingredient}})
    
    if result.modified_count > 0:
        return jsonify({'message': 'maj réussie'}), 200
    else:
        return jsonify({'message': 'maj échouée'}), 400

@personne_bp.route('/<string:username>/vider', methods=['DELETE'])
def vider_liste_course(username):
    result = db.personne.update_one({"username": username}, {"$set": {"liste_course": []}})
    
    if result.modified_count > 0:
        return jsonify({'message': 'maj réussie'}), 200
    else:
        return jsonify({'message': 'maj échouée'}), 400


@personne_bp.route('/<string:username>/retirer', methods=['PUT'])
def retirer_ingredient(username):
    data = request.get_json()
    ingredient = data.get('ingredient')
    
    result = db.personne.update_one({"username": username}, {"$pull": {"liste_course": ingredient}})
    
    if result.modified_count > 0:
        return jsonify({'message': f'Retrait de {ingredient} réussi pour {username}'}), 200
    else:
        return jsonify({'message': f'{ingredient} n\'a pas été trouvé dans la liste de courses de {username}'}), 404

