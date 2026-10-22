import json

def load_recipes(path):
    with open(path, "r", encoding="utf-8") as f:
        recipes = json.load(f)

    return recipes

if __name__ == "__main__":
    all_recipes = load_recipes("data/recipes.json")
    print(all_recipes["minecraft:torch"]["ingredients"]["minecraft:stick"]["quantity_needed"])
    print(all_recipes["minecraft:coal"])