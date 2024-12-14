import pandas as pd
from pymongo import MongoClient
import sys

client = MongoClient("mongodb://localhost:27017")
db = client["project"]
movie = db["movie"]

def load(movie_csv):
    df_movie = pd.read_csv(movie_csv, skiprows=1, names=['title', 'director', 'country', 'release_year', 'rating', 'duration', 'genre', 'description'])
    df_movie['release_year'] = pd.to_numeric(df_movie['release_year'], errors='coerce')
    df_movie['rating'] = pd.to_numeric(df_movie['rating'], errors='coerce')

    movie_data = df_movie.to_dict(orient='records')

    movie.insert_many(movie_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("please use format: python3 load.py movie.csv")
        sys.exit(1)

    movie_csv = sys.argv[1]

    load(movie_csv)
