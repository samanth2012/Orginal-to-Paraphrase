
# Sentiment Analysis Web Application

This is a simple movie sentiment analysis web application. It determines whether a given word is positive or negative and saves the predictions into a database.

## Installation Process

1. **Create AI Model:**
   - Install Docker for Windows and sign up.
   - Create a Dockerfile and a docker-compose file.
   - Run the following command to create a Django project:
     ```
     docker-compose run web django startproject project_name
     ```

2. **Docker File (Dockerfile):**
   ```dockerfile
   FROM python:3.10.3

   ENV PYTHONBUFFERED 1

   RUN mkdir /app
   WORKDIR /app

   COPY requirements.txt /app/
   RUN pip install -r requirements.txt

   RUN pip install keras tensorflow
   RUN pip install --no-cache-dir mysql-connector-python

   COPY . /app/

   CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

Docker Compose File (docker-compose.yml):
```dockerfile-compose.yaml
version: '3'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
```
Requirements.txt
```requirements.txt
Django==2.2
keras
tensorflow 
matplotlib==3.3.3; platform_system != 'Darwin' and platform_system != 'Windows'
mysql-connector-python==8.0.21

```
```docker configure
Attach Project to Container using this command:
docker-compose up
```
```
Create Django App:
Open Windows PowerShell and create a Django app for the project:
docker exec <image_name> python manage.py startapp app_name
```
```
Configure App in settings.py:
Update the INSTALLED_APPS in the settings.py file to include the newly created app:

python
Copy code
INSTALLED_APPS = [
    # ...
    'app_name',
]
```
```
Database Setup (in settings.py):
Configure the database settings in the settings.py file:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
        'PORT': 'your_database_port',
    }
}
```

View Logic for Model Testing:
Implement logic in views for loading the model and testing it. Handle HTTP methods appropriately, especially POST requests if you are using a form for input.

Finally enable kubernetes in docker desktop


![mysql](https://github.com/samanth2012/sentimentanalaysis/assets/114215621/b96b93a7-b464-4b55-83d5-0f4a1025dd7f)

![MOVIE REVIEW ANALYSIS - Brave 08-12-2023 19_28_13](https://github.com/samanth2012/sentimentanalaysis/assets/114215621/b4a05a95-cfb5-4845-825b-10fa192ee251)

![MOVIE REVIEW ANALYSIS - Brave 08-12-2023 19_28_03](https://github.com/samanth2012/sentimentanalaysis/assets/114215621/101404d2-5495-4da4-84e1-dd10f1e708ac)

