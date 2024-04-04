from personne_route import personne_bp
from recette_route import recette_bp
from flask import Flask
#from flask_cors import CORS


app= Flask(__name__)
#cors = CORS(app)




@app.route('/')
def hello_world():
    return 'Hello, world!!'

app.register_blueprint(recette_bp, url_prefix='/recette')
app.register_blueprint(personne_bp, url_prefix='/personne')
if __name__=='__main__':
    app.run(debug=True)
    


    












