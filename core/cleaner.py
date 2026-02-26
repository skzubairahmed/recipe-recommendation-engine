import os
import json
import re
from inspector import ins

class Cleaner:
    def __init__(self):
        self.absolute_path = ""
        self.raw_vocab = []
        self.clean_vocab = set()
    
    def load_raw_vocab(self, path):
        self.absolute_path = os.path.abspath(path)

        with open(self.absolute_path, 'r') as f:
            self.raw_vocab = json.load(f)
    
    def preprocess(self):
        if self.raw_vocab is str:
            raw_vocab_str = self.raw_vocab
            raw_vocab_json = json.loads(raw_vocab_str)

            with open(self.absolute_path, 'w') as f:
                json.dump(raw_vocab_json, f)

        
