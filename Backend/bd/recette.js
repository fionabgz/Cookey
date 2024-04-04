
db = db.getSiblingDB("SaeDB");
db.recette.drop();


db.recette.insertMany([
	{"_id":1,"nom":"Spaghetti al ragù Giuseppe","temps":45,"nutriscore":"A","nbPersonne":4,"ingredients":
	[
	{"nom":"celeri","nb":2,"unite":"tiges"},
	{"nom":"carotte","nb":2},
	{"nom":"ail","nb":2,"unite":"gousse"},
	{"nom":"concentré de tomate","nb":2,"unite":"c à s"},
	{"nom":"tomate","nb":500,"unite":"g"},
	{"nom":"courgette","nb":1},
	{"nom":"champignon","nb":150,"unite":"g"},
	{"nom":"oignon","nb":1},
	{"nom":"beurre","nb":2,"unite":"c à s"},
	{"nom":"viande haché","nb":500,"unite":"g"},
	{"nom":"laurier","nb":2,"unite":"feuille"},
	{"nom":"spaghetti","nb":400,"unite":"g"},
	{"nom":"persil frisé","nb":0.5,"unite":"botte"},
	{"nom":"emmental râpé","nb":100,"unite":"g"},
	],"instruction": "   1.Lavez les courgettes, les carottes, le céleri et les champignons. Taillez les légumes en brunoise. Faites revenir l’oignon et l’ail dans le beurre. Ajoutez la viande hachée et le concentré de tomates puis laissez mijoter. Ajoutez la brunoise de légumes et laissez-les mijoter Épluchez les tomates et coupez-les en morceaux. Ajoutez-les aux légumes et à la viande hachée. Ajoutez le laurier. Salez et poivrez. Laissez la sauce mijoter pendant 30 min. à feu doux 3.Faites cuire les spaghettis. Servez la sauce dans un bol. Égouttez les spaghettis. Faites fondre une noisette de beurre dans la poêle dans laquelle vous avez préparé la sauce et ajoutez les spaghettis. Remuez 4.Servez les spaghettis avec la sauce et terminez par du persil et de l’emmental ou du gruyère."},
	
	{"_id":2,"nom":"quiche suisse aux oignons","temps":40,"nutriscore":"C","nbPersonne":3,"ingredients":
	[
	{"nom":"oeufs","nb":3},
	{"nom":"gruyère râpé","nb":200,"unite":"g"},
	{"nom":"crème fraiche","nb":25,"unite":"cl"},
	{"nom":"huile d'olive","nb":2,"unite":"c à s"},
	{"nom":"pâte brisée","nb":1},
	{"nom":"oignon","nb":500,"unite":"g"}
	],"instruction": "Hachez grossièrement les oignons et faites-les revenir pendant 2 min. à feu doux dans une sauteuse contenant l’huile. Couvrez et laissez suer 20 min. à feu doux, en mélangeant de temps en temps 2.Préchauffez le four sur th. 6 -180°C 3.Garnissez un grand moule à tarte avec la pâte brisée 4.Battez les œufs en omelette dans un grand saladier, ajoutez la crème, les oignons et le gruyère ; mélangez bien et rectifiez l’assaisonnement. Versez dans le fond de tarte et faites cuire au four pendant 30 min. "}

])
