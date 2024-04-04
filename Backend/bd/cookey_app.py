from flask import Flask
from flask_cors import CORS
from recette_routes import recette_bp

app = Flask(__name__)
CORS(app)  

app.register_blueprint(recette_bp, url_prefix='/recette')

if __name__ == '__main__':
    app.run(debug=True)
