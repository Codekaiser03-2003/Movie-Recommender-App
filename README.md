# Movie Recommender System

A movie recommender system built using Python, Streamlit, and machine learning algorithms. The app recommends movies based on a selected movie by calculating the similarity between movie features. It is deployed on Streamlit Cloud Community.

## Features

- **Movie Recommendations**: Select a movie from the dropdown and get recommended movies based on similarity.
- **Poster Display**: Each recommended movie is displayed with its poster image fetched from The Movie Database (TMDb) API.
- **Fast and Interactive UI**: Powered by Streamlit for a smooth, interactive experience.

## Technologies Used

- **Python**: The main programming language used for building the recommender system.
- **Streamlit**: Used to create the web app for displaying movie recommendations.
- **Pandas**: Used for data manipulation and handling the movie dataset.
- **NumPy**: For handling matrix operations for movie similarity calculation.
- **TMDb API**: For fetching movie posters.

## How It Works

1. **Dataset**: The dataset consists of movies with their features (e.g., title, genre, movie ID, etc.).
2. **Similarity Calculation**: A similarity matrix is computed using a machine learning algorithm. This matrix helps recommend movies based on the selected movie’s features.
3. **Streamlit Interface**: The app uses Streamlit for displaying the movie recommendation interface, allowing users to choose a movie and view the recommended movies and their posters.

## Installation

### Prerequisites

- Python 3.6+
- Required libraries listed in `requirements.txt`.

### Setting Up Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the Streamlit app locally:
    ```bash
    streamlit run app.py

## Deployment

The app is deployed on Streamlit Cloud. You can access it using the following link:

[Movie Recommender System](https://movie-recommender-app-3ovjwirqkfahgbhjhibukk.streamlit.app/)

## Files

- **app.py**: Main Streamlit app file that contains the core logic for the movie recommendation system.
- **movie_dict.pkl**: Pickled movie dataset containing information such as titles, genres, movie IDs, etc.
- **similarity1.pkl**, **similarity2.pkl**: Pickled parts of the movie similarity matrix used to calculate movie recommendations.
- **requirements.txt**: Python dependencies needed to run the app. Install them using `pip install -r requirements.txt`.
- **secrets.toml**: Streamlit secrets for securely managing sensitive information like API keys.

