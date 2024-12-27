import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load the data and preprocess it
data = pd.read_csv('anime.csv', usecols=["genre", "names", "episodes"])



#convert episodes into numerical vectors using TF-IDF TfidfVectorizer.
data["episodes"] = pd.to_numeric(data["episodes"]).astype(int)




#compute cosine similarily between TF-IDF vectors



# function to get recommendations based on cosine similarity
def recommendation(episodes, genre, recommendations=5):
    """
        Get anime recommendations based on genre and episode length.

        input_genre: Genre input from the user
        max_episodes: Maximum number of episodes preferred by the user
        top_n: Number of recommendations to return
        return: List of recommended anime names
        """

    # Create a vector for the input genre

    # Compute similarity between the input and all anime genres

    # Filter based on episode length and sort by similarity

    return []




