## Dajngo ORM Watching Storage
Simple web application on Django, forked from [django-orm-watching-storage](https://github.com/dvmn-tasks/django-orm-watching-storage).
This app could be used with outside database with visits and access cards of your workers.

Project was created as first lesson in [module Django ORM](https://dvmn.org/modules/django-orm/) by [Devman](https://dvmn.org).

### How to install
Clone repo from github:
```
git clone https://github.com/ekbdizzy/django-orm-watching-storage
```

Create and activate [virtualenv](https://virtualenv.pypa.io/en/latest/) for your project:
```
# Install virtualenv if not installed.
python3 -m pip install virtualenv

# Create virtualenv 
cd django-orm-watching-storage
python3 -m virtualenv venv
venv/bin/pip install -r requirements.txt
```
Create .env file inside your project folder (default folder is django-orm-watching-storage)
``` 
touch .env
```
Add variables to .env:
```
SECRET_KEY=SECRET_KEY  # your awesome secret key.
DEBUG=True  # use True only for development, use False for production.
ALLOWED_HOSTS=localhost  # list of your allowed hosts, add with comma (host1,host2,host3)
DB=postgres://USER:PASSWORD@HOST:PORT/NAME  # see more https://github.com/jacobian/dj-database-url
```
Run project:
```
venv/bin/python manage.py runserver
```

### Warning
You have not access to Database, so you can't use this service as is.
But you are free to use this code and learn methods used to make requests to database.

