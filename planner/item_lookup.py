import loader

def is_raw_material(recipe_dict, item_id):
    if item_id in recipe_dict:
        return False
    else:
        return True

recipe_dict = loader.load_recipes("data/recipes.json")
print(is_raw_material(recipe_dict, "minecraft:coal"))
print(is_raw_material(recipe_dict, "minecraft:torch"))
print(is_raw_material(recipe_dict, "minecraft:tourch"))