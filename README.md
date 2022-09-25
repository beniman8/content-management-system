# content-management-system
This is a django simple content management system 

## Basic Overview

## Commands to start this pojects in your window terminal

This here are the commands to start th project

when you name your project make sure to put a space and a dot -> . 
so that your manage.py file starts on your working directory instead of 
your project direcory.This makes it easier to work with.

```bash
virtualenv Env

Env\Scripts\activate    

pip install django
pip install decouple

pip freeze > requirements.txt

django-admin startproject core .
```

## .env file content 

You have to create a .env file in your directory at the same location the manage.py exists.

remove the '' when you copy your SECURITY_KEY to the .env file

```.env

SECRET_KEY=paste-your-security-key-here
DEBUG=True

ALLOWED_HOSTS=127.0.0.1, localhost

NAME=your-db-name
USER=your-db-username
PASSWORD=your-db-password
HOST=your-db-host

EMAIL_HOST=your-email-host
EMAIL_PORT=your-email-port
EMAIL_HOST_PASSWORD=your-email-host-password
EMAIL_HOST_USER=your-email-host-user



```


### Setings.py

import config and Csv from decouple 
Replace your secret key, debu abd allowed host to match your .env file 

you can see now we are using config to fetch the data from our .env file.
Now we can get our secret information only in our local host or server

```python
from pathlib import Path
from decouple import config , Csv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

```