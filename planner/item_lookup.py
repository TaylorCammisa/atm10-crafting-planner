import loader

def is_raw_material(recipes, item_id):
    if item_id in recipes:
        return False
    else:
        return True

if __name__ == "__main__":
    recipes = loader.load_recipes("data/recipes.json")
    print(is_raw_material(recipes, "minecraft:coal"))
    print(is_raw_material(recipes, "minecraft:torch"))
    print(is_raw_material(recipes, "minecraft:tourch"))