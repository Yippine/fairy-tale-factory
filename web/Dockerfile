FROM python:3.9
WORKDIR /web
COPY . /web
RUN  apt-get update\
      && apt-get install -y build-essential\
      && pip install --upgrade pip\
      && pip install uwsgi\
      && pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
CMD ["sh", "-c", "python manage.py collectstatic --no-input && uwsgi --chdir=/web --module=project.wsgi:application --http-socket=0.0.0.0:8000 --threads=3 --static-map /static=/web/static"]
