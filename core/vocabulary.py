import json
import os

class Vocabulary:
    def __init__(self):
        self.unique_ingredients = set()
        self.sorted_vocab = []
        self.ingredients_raw = []
        self.absolute_path = ""
    
    def load_dataset(self, path):
        self.absolute_path = os.path.abspath(path)
        os.error("Hello")
        with open(self.absolute_path, 'r') as f:
            self.ingredients_raw = json.load(f)

    def build_master_vocab(self):
        for recipe in self.ingredients_raw:
            for ingredient in recipe['ingredients']:
                clean_ingredient_name = (ingredient.lower().strip())
                print(clean_ingredient_name)
                self.unique_ingredients.add((clean_ingredient_name))
        
        self.sorted_vocab = sorted(list(self.unique_ingredients))

        return self.sorted_vocab
    