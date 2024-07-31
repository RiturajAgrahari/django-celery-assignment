__Hi there!, How are you doing?__

__I hope you doing well :)__

# Django-Celery-Redis Integration WebApp
In this project i leverage django to make an webapp which uses Stability AI to generate text-to-image by using redis
broker and celery, the app is now scalable horizontally and performance is enhanced due to celery and redis library
.

___Note: This project is compatible with Windows along with docker.___

## Technologies used:
* Django
* Docker
* Celery
* Redis
* Stability AI

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

* Create a .env file and adding these details into it :

```
DJANGO_SECRET_KEY = "your_django_secret_key"
STABILITY_API_KEY = "your_stability_api_key"
CELERY_BROKER_REDIS_URL = "redis://redis:6379"
```

__API KEY__: https://platform.stability.ai/docs/api-reference#tag/Text-to-Image/operation/textToImage

* Now we will make migrations to initiate our sql lite db
```
python manage.py makemigrations
python manage.py migrate
```

* __Additional Note:__ Create a `media` dir in main directory

### Docker configuration
* _here i used docker desktop for windows_
* all docker config files are already included in the repo
* Run this command to start the docker :

```docker-compose up -d --build```

### Done!
* ___The project will be on http://127.0.0.1:8001/___
* There is very little delay in updation of history/images because django-channels are not used in this project.

### Extro :
The project is fully tested and it is working completely fine, but as a developer i know what can 
be possibly happen, so i have a gentle request, if you find any mistake or if you find anything wrong in this
or if you think this is a not the best way to do that, please drop a message i would love when i get to know about 
my mistakes, because after you i will never want anyone to point the same mistake again.


### Thankyou :
Thankyou so much for watching this repo, have a nice day forever

### You can skip this:
* __This is not a production build. It will work on locally only.__
* It is only designed to do the specified task, otherwise it can be way more better than the current stage.
* Some steps can be done in different way as well, but i found this to be the best approach to accomplish the specified task.
* It is completed tested
