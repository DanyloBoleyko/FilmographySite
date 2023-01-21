# FilmographySite
Site which helps people to see producers' films, actors and films where they starred at.

## Database
![DB schema](https://github.com/DanyloBoleyko/FilmographySite/blob/main/FilmographyDB.drawio.svg?raw=true)

## Setup project

1. Clone repository.
2. Setup and activate virtual environment.
    ```
    python -m venv venv
    ./venv/Scripts/activate
    ```
3. Install all required packages to venv:
    ```
    pip install -r requirements.txt
    pip freeze > requirements.txt
    ```
4. Run server:
    ```
    python filmography/manage.py runserver
    ```
