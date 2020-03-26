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
    
- Setup standard migration inside app folder:
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
    
- Setup database installing psycopg2 for PostgreSQL:
    `pip install psycopg2`
    
- Setup Django:
    `python -m pip install Django`
    
- Setup standard migration inside app folder:
    `python manage.py migrate`

-------
    
- Start server:
    `python manage.py runserver`
    
- Run feature test:
    `./manage.py test movies_db.tests`

-------
    
    
