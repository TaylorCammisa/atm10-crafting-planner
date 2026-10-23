import loader

def is_raw_material(recipes, item_id):
    return item_id not in recipes

if __name__ == "__main__":
    recipes = loader.load_recipes("data/recipes.json")
    print(is_raw_material(recipes, "minecraft:coal"))
    print(is_raw_material(recipes, "minecraft:torch"))
    print(is_raw_material(recipes, "minecraft:tourch"))