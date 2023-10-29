FROM python:slim
LABEL authors="alecs"

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements/dev.txt .
RUN pip install --upgrade pip \
    && pip install -r dev.txt

# copy project
COPY . .

#CMD ["sh", "-c", "python manage.py makemigrations --settings=mysite.settings.dev && python manage.py migrate --settings=mysite.settings.dev"]
#CMD python manage.py shell --settings=mysite.settings.dev -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '123qwe')"
#CMD ["sh", "-c", "DJANGO_SETTINGS_MODULE=mysite.settings.dev gunicorn mysite.wsgi:application --bind 0.0.0.0:8000"]
