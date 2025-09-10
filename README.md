🎌 Anime Recommendation System

A web-based Anime Recommendation System built with Flask that recommends anime shows and movies based on user preferences. The system leverages cosine similarity for accurate recommendations and integrates a large-scale dataset of around 12,000 anime titles.

🚀 Features

🔑 User Authentication – Register and log in to manage your profile.
🎥 Content-Based Recommendations – Uses cosine similarity to suggest anime titles based on what you like.
📊 Large Dataset Integration – Supports 12,000+ shows and movies for broad and diverse recommendations.

🛠️ Tech Stack

Backend: Flask (Python)
Database: SQLAlchemy
Recommendation Engine: Cosine Similarity (scikit-learn, NumPy, pandas)
Frontend: HTML, CSS, Bootstrap
Version Control: Git & GitHub

🧮 How It Works

1. User Login/Signup – Users register and log in.
2. Input/Selection – Users can search or choose anime titles.
3. Recommendation Engine –
   Extracts features from the dataset.
   Computes cosine similarity between titles.
   Ranks the most relevant shows.
4. Result Display – Presents the top recommended anime titles.

📊 Dataset

Size: Around 12,000 anime titles (combined shows + movies).
Attributes: Title, Genre, and Ratings.
