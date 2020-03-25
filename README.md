- Setup project:
    `django-admin startproject app`
    
- Initialize git repo and add .gitignore file
    
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
    
- Start server:
    `python manage.py runserver`
    
- Create the app(in the same dir of manage.py):
    `python manage.py startapp nameofapp`