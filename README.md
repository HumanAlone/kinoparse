# Задание "Парсинг кинопоиска. Заливка в neo4j."

В работе использован сервсис https://kinopoiskapiunofficial.tech  

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

<img width="534" alt="Снимок экрана 2024-01-09 в 12 30 21" src="https://github.com/HumanAlone/kinoparse/assets/19314596/465d8c93-43e8-41f0-8c7b-6af206c138c0">  


<img width="391" alt="Снимок экрана 2024-01-09 в 12 37 53" src="https://github.com/HumanAlone/kinoparse/assets/19314596/2d316c4d-aae1-40f9-93f3-07fda3267b15">

<img width="2001" alt="Снимок экрана 2024-01-09 в 12 54 47" src="https://github.com/HumanAlone/kinoparse/assets/19314596/db74eb18-b6dd-4e91-ac56-efa15adb62d7">
