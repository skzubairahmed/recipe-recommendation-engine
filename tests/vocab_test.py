from core.vocabulary import Vocabulary
import json
import os

vc = Vocabulary()

def test_vocabulary():
    test_filename = "raw_test.json"
    sample_data = [
        {"ingredients": ["Salt", "Pepper", "pepper"]}, 
        {"ingredients": ["CHICKEN", "salt"]}           
    ]
    
    for i in range(0, 9999999):
        with open(test_filename, 'w') as f:
            json.dump(sample_data, f)
    
        vocab = vc.build_master_vocab(test_filename)

        if i == 2785:
            print("error in 2785")

        assert vocab[0] == "chicken"
        assert vocab == sorted(vocab)
        assert len(vocab) == 3
        assert "salt" in vocab
        assert "Salt" not in vocab