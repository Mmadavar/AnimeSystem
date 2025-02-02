import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load the data and preprocess it
data = pd.read_csv('anime.csv', usecols=["genre", "name", "episodes"])

#convert episodes into numerical vectors using TF-IDF TfidfVectorizer.
data["episodes"] = pd.to_numeric(data["episodes"], errors='coerce').fillna(0).astype(int)
data["genre"] = data["genre"].fillna("").str.lower()

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data["genre"])


# function to get recommendations based on cosine similarity
def recommendation(episodes, genre, total):

    # tranform input genre into a vector
    input_vector = tfidf.transform([genre.lower()])

    # Compute similarity between the input and all anime genres
    genre_similarities = cosine_similarity(input_vector, tfidf_matrix).flatten()

    # Filter based on episode length and sort by similarity
    data["similarity"] = genre_similarities
    filtered_df = data[data["episodes"] <= episodes]
    recommendations = filtered_df.sort_values(by="similarity", ascending=False)

    return recommendations.head(total)[["name", "genre", "episodes"]]




