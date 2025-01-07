import streamlit as st  # Importing Streamlit for creating the web application interface
import pickle  # Importing pickle to load saved objects like movie data and similarity matrix
import pandas as pd  # Importing pandas to handle data in DataFrame format


# Function to recommend movies
def recommend(movie):
    # Find the index of the selected movie in the 'movies' DataFrame based on the movie's title
    index = movies[movies['title'] == movie].index[0]

    # Sort the cosine similarity scores for the selected movie in descending order.
    # 'enumerate' creates an index, so we get the index and the similarity value of each movie compared to the selected movie
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    # List to store recommended movies
    recommended_movies = []

    # Loop through the sorted list of distances (excluding the first one, which is the movie itself)
    for i in distances[1:6]:  # Get the top 5 recommendations
        recommended_movies.append(movies.iloc[i[0]].title)  # Add movie titles to the list of recommendations
    return recommended_movies  # Return the list of recommended movie titles


# Load the movie dictionary and similarity matrix from the saved pickle files
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))  # Load movie data (a dictionary format) from 'movie_dict.pkl'
movies = pd.DataFrame(movies_dict)  # Convert the movie data to a pandas DataFrame for easier manipulation
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Load the cosine similarity matrix from 'similarity.pkl'

# Streamlit UI components
st.title('Movie Recommendation System')  # Display the title of the app

# Create a dropdown to select a movie from the 'movies' DataFrame
selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values  # Provide all movie titles as options in the dropdown
)

# When the 'Recommend' button is clicked, display the recommended movies
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)  # Call the recommend function
    st.write("Here are your recommended movies:")  # Display a message
    for movie in recommendations:  # Loop through the recommended movies
        st.write(movie)  # Display each recommended movie title
