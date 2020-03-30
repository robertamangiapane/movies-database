## SETUP A DJANGO PROJECT FROM SCRATCH

- Initialize git repo and add .gitignore file

- Setup project:
    `django-admin startproject app`
        
- Setup venv:
    `python3 -m venv venv`
    
- Activate venv:
    `source venv/bin/activate`
    
- Setup database installing psycopg2 for PostgreSQL:
    `pip install psycopg2`
    
- Setup Django:
    `python -m pip install Django`
    
- Create Database:
    `psql postgres`
    `CREATE DATABASE my_movies_db`
    
- Setup standard migrations inside app folder:
    `python manage.py migrate`
    
- Setup project migrations (every time you change your model):
    `python manage.py makemigrations movies_db`
    `python manage.py migrate`
    
- Create the app(in the same dir of manage.py):
    `python manage.py startapp movies_db`
    
--------
    
## OR CLONE THE REPO

- Git clone:
    `git clone git@github.com:robertamangiapane/movies-database.git`

- `cd movies-database`

- Setup venv:
    `python3 -m venv venv`
    
- Activate venv:
    `source venv/bin/activate`
    
- Add .gitignore file
    
- Setup database installing psycopg2 for PostgreSQL:
    `pip install psycopg2`
    
- Setup Django:
    `python -m pip install Django`
    
- Set up PostgreSQL: Install PostgreSQL if you don't have it on your local machine. The application works only with no password set and 'postgres' default user
- Create Database:
    `psql postgres`
    `CREATE DATABASE my_movies_db`
    
- Setup standard migrations inside app folder:
    `python manage.py migrate`
    
- Setup project migrations (every time you change your model):
    `python manage.py makemigrations movies_db`
    `python manage.py migrate`

-------
    
- Start server:
    `python manage.py runserver`
    
- Run feature test:
    `./manage.py test movies_db.tests`

-------
    
    
