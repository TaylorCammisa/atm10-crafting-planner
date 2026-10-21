import json

with open("data/recipes.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

print(recipes["minecraft:torch"]["ingredients"]["minecraft:stick"]["quantity_needed"])