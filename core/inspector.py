import os
import json

class Inspector:
    def __init__(self):
        self.absolute_path = ""
        self.vocab = []

    def load_vocab(self, path):
        self.absolute_path = os.path.abspath(path)
        
        with open(self.absolute_path, 'r') as f:
            self.vocab = json.load(f)
    
    def inspect_vocab(self):
        for ing in self.vocab:
            print(ing)
    
    def inspect_specified(self, index):
        print(self.vocab[index])

