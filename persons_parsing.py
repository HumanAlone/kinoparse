import json
from time import sleep

import requests

with open("films.json") as f_inp:
    films = json.load(f_inp)

token = ""  # Add your own token
header = {"x-api-key": token}


film_ids = (dict_.get("kinopoiskId") for dict_ in films)

staff = []
for film_id in film_ids:
    url = f"https://kinopoiskapiunofficial.tech/api/v1/staff?filmId={film_id}"
    request = requests.get(url, headers=header)
    req_json = request.json()
    for person in req_json:
        person["kinopoiskId"] = film_id
    staff += req_json
    sleep(0.2)

unique_staff = []
for person in staff:
    if person not in unique_staff:
        unique_staff.append(person)

staff_res = json.dumps(unique_staff)
with open("staff.json", "w", encoding="utf8") as f_out:
    f_out.write(staff_res)
