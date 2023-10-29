# Mysite

Сайт с различными приложениями <br>
Получить доступ можно по ссылке: https://alecs.pythonanywhere.com/


## Quickstart

Run the following commands to bootstrap your environment:
    
    sudo apt get update
    sudo apt-get install -y git python3-dev python3-venv python3-pip vim
    git clone https://github.com/alecsbeinar/MySite
    cd mysite
      
    python3 -m venv venv   
    source venv/bin/activate
    pip3 install -r requirements/prod.txt 

    mysql> CREATE DATABASE ads;
        create user 'user'@'localhost' IDENTIFIED BY 'your-password';
        GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';
        FLUSH PRIVILEGES;

    cp .env.template .env
    Set all variables and export them

    python manage.py migrate --settings=mysite.settings.prod

Run the app locally:

    python3 manage.py runserver 0.0.0.0:8000 --settings=mysite.settings.prod

Run the app with gunicorn:

    gunicorn mysite.wsgi -b 0.0.0.0:8000

## Docker

docker-compose up

### MySite usage:

Get a list of questions from Polls API:
    
    python3 manage.py shell

    >>>> from polls.models import Question
    >>>> Question.objects.all()
    >>>> 


