import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load the data and preprocess it
data = pd.read_csv('anime.csv', usecols=["genre", "names", "episodes"])



#convert episodes into numerical vectors using TF-IDF TfidfVectorizer.
data["episodes"] = pd.to_numeric(data["episodes"]).astype(int)

df = TfidfVectorizer(stop_words='english')
df_matrix = df.fit_transform(data["episodes"])


#compute cosine similarily between TF-IDF vectors
cosine_sim = cosine_similarity(df_matrix)


# function to get recommendations based on cosine similarity
def recommendation(episodes, genre, recommendations=5):

    # Create a vector for the input genre
    input_vector = df.transform([genre])

    # Compute similarity between the input and all anime genres
    genre_similarities = cosine_similarity(input_vector, df_matrix).flatten()

    # Filter based on episode length and sort by similarity
    df["similarity"] = genre_similarities
    filtered_df = df[df["episodes"] <= episodes]
    recommendations = filtered_df.sort_values(by="similarity", ascending=False).head(recommendations)

    return recommendations["name"].tolist()




