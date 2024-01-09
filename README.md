# Задание "Парсинг кинопоиска. Заливка в neo4j."

В работе использован сервси https://kinopoiskapiunofficial.tech  

Сначала были получены списки стран и жанров по эндпоинту /api/v2.2/films/filters.  
По эндпоинту /api/v2.2/films получен список фильмов.  
По эндпоинту /api/v1/staff получена информация об актёрах, режиссёрах и прочих сотрудниках.  

## Как работает?

films_parsing.py собирает данные о фильмах.  
persons_parsing.py собирает данные о людях.  
neo4j_service.py отвечает за загрузку данных в neo4j.  

## Собранные данные.
countries.json содержит данные о странах.  
genres.json содержит данные о жанрах.  
films.json содержит данные о фильмах.  
staff.json содержит данные о персонале (режиссёры, актёры и т.д.).
