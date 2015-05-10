import media
import fresh_tomatoes
import json
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
path_to_movies_json = os.path.join(script_dir, 'data/movies.json')

with open(path_to_movies_json) as json_file:
    movies_json = json.load(json_file)

movies = []

# parse elements of json file into media.Movie objects
for movie_json in movies_json["movies"]:
    movies.append(media.Movie(movie_json))

fresh_tomatoes.open_movies_page(movies)
