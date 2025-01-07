# movie-recommendation-system
A machine learning-based movie recommendation system that suggests similar movies based on the given movie title by analyzing movie metadata such as genres, keywords, and cast.
# Movie Recommendation System

This project is a **Movie Recommendation System** built using machine learning techniques. It takes in user input in the form of a movie name and recommends similar movies based on their attributes, such as genres, keywords, and cast. The recommendation system uses cosine similarity to calculate the similarity between movies.

## Features

- **Movie Recommendations**: Recommends top 5 similar movies based on a given movie.
- **Data Processing**: The system processes movie metadata (genres, keywords, cast, crew) and uses natural language processing (NLP) techniques.
- **Cosine Similarity**: Measures the similarity between movies using cosine similarity.
- **Streamlit UI**: Simple and interactive web interface for selecting a movie and viewing recommendations.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Git
- Git LFS (Large File Storage)

**How It Works**

The system loads movie data from a CSV file containing metadata about movies and another CSV for the cast and crew.
The data is processed by converting text data (genres, keywords, etc.) into a structured format.
The recommendation algorithm calculates cosine similarity between the movies based on their attributes.
The user selects a movie from the dropdown in the Streamlit UI, and the system recommends similar movies.

**Acknowledgments**
Inspired by movie recommendation algorithms used by Netflix and other streaming platforms.
Thanks to all open-source contributors who made tools like Scikit-learn and Streamlit available.
