Hi there!, How are you doing?
I hope you doing well :)

# Django-Celery-Redis Integration App
In this project i leverages the value of celery, redis, docker and django to use stability AI API by doing parallel
processing.!

___Note: This project is compatible with Windows along with docker.___

## Let's get started
### First we start with basic django configurations:

*  Creating Virtual Environment :

```python -m venv venv```

* Activating Virtual Environment :

```.\venv\Scripts\activate```

* Cloning the repo :

```git clone https://github.com/RiturajAgrahari/django-celery-assignment.git```

* Installing the requirements :

```pip install -r requirements.txt```

* Create a .env file and add these data into it :

```
DJANGO_SECRET_KEY = "your_django_secret_key"
STABILITY_API_KEY = "your_stability_api_key"
CELERY_BROKER_REDIS_URL = "redis://redis:6379"
```

__API KEY__: https://platform.stability.ai/docs/api-reference#tag/Text-to-Image/operation/textToImage

* Now we will make migrations to initiate our sql lite db
```
python manage.py makimigrations
python manage.py migrate
```

### Docker configuration is attached in the repo as well
* _here i used docker desktop for windows_

