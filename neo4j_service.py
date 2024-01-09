import json

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

NEO4J_URI = ""  # Add your own URI
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = ""  # Add your own password

URI = NEO4J_URI
AUTH = (NEO4J_USERNAME, NEO4J_PASSWORD)

try:
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with open("staff.json", encoding="utf-8") as f_inp:
            staff = json.load(f_inp)
        for person in staff:
            driver.execute_query(
                """CREATE (p:Person {
                            staffId: $staffId,
                            nameRu: $nameRu,
                            nameEn: $nameEn,
                            description: $description,
                            posterUrl: $posterUrl,
                            professionText: $professionText
                            })""",
                staffId=person.get("staffId"),
                nameRu=person.get("nameRu"),
                nameEn=person.get("nameEn"),
                description=person.get("description"),
                posterUrl=person.get("posterUrl"),
                professionText=person.get("professionText"),
            )

        with open("films.json", encoding="utf-8") as f_inp:
            films = json.load(f_inp)
        for film in films:
            driver.execute_query(
                """CREATE (m:Movie {
                            kinopoiskId: $kinopoiskId,
                            imdbId: $imdbId,
                            nameRu: $nameRu,
                            nameEn: $nameEn,
                            nameOriginal: $nameOriginal,
                            countries: $countries,
                            genres: $genres,
                            ratingKinopoisk: $ratingKinopoisk,
                            ratingImdb: $ratingImdb,
                            year: $year,
                            type: $type,
                            posterUrl: $posterUrl,
                            posterUrlPreview: $posterUrlPreview
                            })""",
                kinopoiskId=film.get("kinopoiskId"),
                imdbId=film.get("imdbId"),
                nameRu=film.get("nameRu"),
                nameEn=film.get("nameEn"),
                nameOriginal=film.get("nameOriginal"),
                countries=[dict_.get("country") for dict_ in film.get("countries", {})],
                genres=[dict_.get("genre") for dict_ in film.get("genres", {})],
                ratingKinopoisk=film.get("ratingKinopoisk"),
                ratingImdb=film.get("ratingImdb"),
                year=film.get("year"),
                type=film.get("type"),
                posterUrl=film.get("posterUrl"),
                posterUrlPreview=film.get("posterUrlPreview"),
            )

        with driver.session() as session:
            relations = {
                "WRITER": "WRITED",
                "COMPOSER": "COMPOSED",
                "TRANSLATOR": "TRANSLATED",
                "PRODUCER_USSR": "USSR_PRODUCED",
                "PRODUCER": "PRODUCED",
                "DIRECTOR": "DIRECTED",
                "VOICE_DIRECTOR": "VOICE_DIRECTED",
                "EDITOR": "EDITED",
                "OPERATOR": "SHOT",
                "DESIGN": "DESIGNED",
                "ACTOR": "ACTED_IN",
                "NULL": "UNKNOWN",
            }
            with session.begin_transaction() as tx:
                for person in staff:
                    relationship_type = relations.get(
                        person.get("professionKey", "NULL")
                    )
                    query = (
                        f"MATCH (p:Person {{staffId: {person['staffId']}}}), "
                        f"(m:Movie {{kinopoiskId: {person['kinopoiskId']}}}) "
                        f"CREATE (p)-[:{relationship_type}]->(m)"
                    )
                    tx.run(query)
except ServiceUnavailable:
    print("Ничего не работает. Надо запустить инстанс АурыДб.")
