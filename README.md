We will start by creating an virtual env from terminal
to create a virtual environment :

```python -m venv venv```

and to activate the virtual environment

```.\venv\Scripts\activate```

then we will install the necessary packages from requirements.txt

```pip install -r requirements.txt```

then we will create our djnago project by writing:

```django-admin startproject assignment .```

then we will create our first app in the project

```python manage.py startapp aigeneration```


now first we will change some things from settings.py

adding the app to installed_app
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aigeneration'
]
```

then we will link our project urls.py to our app urls.py
```diff
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("aigeneration.urls"))  # linking our apps urls.py
]
```


now we are going to create migrations in our sql lite db:
```commandline
python manage.py makimigrations
python manage.py migrate
```


Don't forget to add the .env file with these detail 
```
DJANGO_SECRET_KEY = "your_django_secret_key"
API_KEY = "your_api_key_for_image_generation_api"
```
