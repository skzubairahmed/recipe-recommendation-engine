import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_json("./recipe_dataset.json")

df['ingredient_text'] = df['ingredients'].apply(lambda x: ' '.join(x))

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['ingredient_text'])

def get_recommendations(user_input, top_n=5):
    user_tfidf = tfidf.transform([user_input])

    similarity_scores = cosine_similarity(user_tfidf, tfidf_matrix)
    similar_indices = similarity_scores.argsort()[0][::-1]

    return df.iloc[similar_indices[:top_n]]

get_recommendations("eggs")
