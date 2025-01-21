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
   pip install -r requirements.txt

3. Run the Streamlit app locally:
   streamlit run app.py

