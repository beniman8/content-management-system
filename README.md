
<img src="https://github.com/beniman8/content-management-system/blob/main/django_crm.png">

# Customer Relationship Management
This is a django simple customer relationship management is a process in which a business or other organization administers its interactions with customers, typically using data analysis to study large amounts of information.


<br>

## Basic Overview
This website can create agents and leads. 
we can assign leads to each agents
agent can manage their own leads 


<br>

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

<br>

## .env file content 

You have to create a .env file in your directory at the same location the manage.py exists.

remove the commas '' when you copy your SECURITY_KEY to the .env file

<img src="https://github.com/beniman8/content-management-system/blob/main/envfilelocation.PNG" width=40%>

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

<br>

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

## Runing the project locally

Make sure your virtual env is activated and run this command on your terminal.

Make sure also that you are running the command at the same directory as your manage.py folder or it won't work.

To quit project press control C on windows computer ctrl+C

```python

python manage.py runserver

```

## Creating an app

This is how to create apps.

Make sure to change app_name to the name you want your app to be

```bash

python manage.py startapp app_name
```

Once the app is created you will see it in the same directory as your project fille.
In our case in the same folder as core

Make sure to add your app into the setting installed apps in order for django to make use of your new app.

```python

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    'app_name',
]


```

replace the app_name with the name of your app.



## Creating models

A model is data that you want stored in your database in order for you to use later on.
Thing like a person's name, email and etc

To create a model go to your new app open the folder to find the models.py file.

app_name/models.py 

Replace the ModelName to the name you wnat. 
Your model should be a singular noun  ex: boat instead of boat.

```python

from django.db import models

class ModelName(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

```

After your model has been created , you need to migrate it in your database.

Run these commands on your terminal to migrate your new model in to your database.

hint: Django comes with an sqlite3 database that we use in local development.


```python
python manage.py makemigrations
python manage.py migrate
```

Result:

check the folder : app_name/migrations/0001_initial.py

```results

# Generated by Django 3.2.5 on 2022-09-25 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]


```

This is what django will passed down to your detabase.