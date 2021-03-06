FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PORT=8000
ENV DJANGO_DEBUG=false

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

RUN python3 manage.py collectstatic --noinput

EXPOSE $PORT

CMD ["sh", "-c", "uvicorn lit.asgi:application --port ${PORT} --host 0.0.0.0"]
# https://stackoverflow.com/a/54504297
