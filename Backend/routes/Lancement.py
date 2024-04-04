from flask import Flask
from personne_route import personne_bp
from recette_route import recette_bp

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello, Welcome!!'

app.register_blueprint(recette_bp, url_prefix='/recette')
app.register_blueprint(personne_bp, url_prefix='/personne')

if __name__ == '__main__':
    app.run(debug=True)
    