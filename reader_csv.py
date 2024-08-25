import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#load the data and preprocess it
df = pd.read_csv('anime.csv', usecols=["genre"])
print(df)

#convert genres into numerical vectors using TF-IDF
TfidfVectorizer.

#compute cosine similarily between TF-IDF vectors

# get recommendations based on cosine similarity



#get recommendations from a given anime

