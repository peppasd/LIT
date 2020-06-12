FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PORT=8000

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE $PORT

CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:${PORT}"]
# https://stackoverflow.com/a/54504297
