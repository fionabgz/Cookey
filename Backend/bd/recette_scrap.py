import requests
import json

def get_random_recipe():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    data = response.json()
    return data["meals"][0]

def format_recipe(recipe):
    formatted_recipe = {
        "_id": recipe["idMeal"],
        "nom": recipe["strMeal"],
        "temps": int(recipe["strInstructions"].count(".") / 3 * 15),  # Assume 3 steps per minute
        "nutriscore": "A",  # You can add logic to calculate nutriscore based on ingredients
        "nbPersonne": 4,    # You can modify this according to the recipe or extract from API if available
        "ingredients": [],
        "instruction": recipe["strInstructions"]
    }
    # Extracting ingredients
    for i in range(1, 21):  # Assume maximum 20 ingredients
        ingredient_name = recipe[f"strIngredient{i}"]
        ingredient_measure = recipe[f"strMeasure{i}"]
        if ingredient_name and ingredient_measure:
            ingredient = {
                "nom": ingredient_name,
                "nb": ingredient_measure.split()[0],  # Extracting number from measure
                "unite": ingredient_measure.split(maxsplit=1)[1] if len(ingredient_measure.split()) > 1 else None
            }
            formatted_recipe["ingredients"].append(ingredient)
        else:
            break  # No more ingredients
    return formatted_recipe

# Get a random recipe from TheMealDB API
random_recipe_data = get_random_recipe()

# Format the recipe data
formatted_recipe = format_recipe(random_recipe_data)

# Print the formatted recipe
print(json.dumps(formatted_recipe, indent=4))
