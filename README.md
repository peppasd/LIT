# LIT
LabelIT. An image labeling website. Created for the TU Berlin SkSys module.

##  Development Guide

* [Install Docker](https://docs.docker.com/get-docker/)
* In the root directory of the project:
```bash
    $ docker-compose build      # Build the containers
    $ docker-compose up         # Run the container
```
* The django instance should run on port 8000 and pgadmin on port 80 (HTTP)
* To run any command in the django container, eg migrate:
```bash
    $ docker-compose run web python manage.py migrate  # docker-compose run web <your command>
```
