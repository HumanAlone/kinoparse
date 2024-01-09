import json
from time import sleep

import requests

token = ""  # Add your own token
header = {"x-api-key": token}


with open("genres.json") as f_inp:
    genres = json.load(f_inp)

genre_ids = [dict_.get("id") for dict_ in genres]

films = []
for genre in genre_ids:
    url = f"https://kinopoiskapiunofficial.tech/api/v2.2/films?genres={genre}&order=RATING&type=FILM&ratingFrom=0&ratingTo=10&yearFrom=1000&yearTo=3000&page=1"
    request = requests.get(url, headers=header)
    req_json = request.json()
    pages_count = req_json.get("totalPages", 1)
    content = req_json.get("items", [])
    if content:
        films += content
    for page in range(2, pages_count + 1):
        url = f"https://kinopoiskapiunofficial.tech/api/v2.2/films?genres={genre}&order=RATING&type=FILM&ratingFrom=0&ratingTo=10&yearFrom=1000&yearTo=3000&page={page}"
        request = requests.get(url, headers=header)
        content = req_json.get("items", [])
        films += content
        sleep(0.5)

unique_films = []
for film in films:
    if film not in unique_films:
        unique_films.append(film)

films_res = json.dumps(unique_films)
with open("films.json", "w", encoding="utf8") as f_out:
    f_out.write(films_res)
