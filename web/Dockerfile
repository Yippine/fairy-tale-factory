# # FROM python:3.9
# # WORKDIR /web
# # COPY . /web
# # RUN  apt-get update\
# #       && apt-get install -y build-essential\
# #       && pip install --upgrade pip\
# #      && pip install uwsgi\
# #      && pip install -r requirements.txt

# # CMD ["sh", "-c","uwsgi -w manage:app --http-socket :8000 --threads 5"]


# FROM python:3.9
# WORKDIR /web
# COPY . /web
# RUN  apt-get update\
#       && apt-get install -y build-essential\
#       && pip install --upgrade pip\
#       && pip install uwsgi\
#       && pip install -r requirements.txt


# ENV PYTHONUNBUFFERED 1

# # CMD指令改成使用uWSGI啟動伺服器
# # CMD ["uwsgi", "--socket", ":8000", "--module", "manage.wsgi:application", "--static-map", "/static=/project/static"]
# CMD ["uwsgi", "--ini", "uwsgi.ini"]

# # RUN sed -i 's/\r//' ./start.sh
 
# # 设置start.sh文件可执行权限
# # RUN chmod +x ./start.sh



FROM python:3.9
WORKDIR /web
COPY . /web
RUN  apt-get update\
      && apt-get install -y build-essential\
      && pip install --upgrade pip\
      && pip install uwsgi\
      && pip install -r requirements.txt


ENV PYTHONUNBUFFERED 1

# CMD ["sh", "-c", "python manage.py collectstatic --no-input && uwsgi --chdir=/web --module=project.wsgi:application --http-socket=0.0.0.0:8000 --processes=4 --threads=3"]

CMD ["sh", "-c", "python manage.py collectstatic --no-input && uwsgi --chdir=/web --module=project.wsgi:application --http-socket=0.0.0.0:8000 --threads=3 --static-map /static=/web/static"]