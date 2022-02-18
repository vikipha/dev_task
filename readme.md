## PDF Service skeleton
Contains basic configuration of Django server with already set up postgresql database.


### Basic commands

build/rebuild docker image

`docker-compose build`

run api server

`docker-compose up`

run tests:

`docker-compose run api /opt/bin/run_tests.sh`

run mypy:

`docker-compose run api /opt/bin/run_mypy.sh`


### Connecting to DB from outside
Postgres database is running inside container. If you want to connect to it,
you can either connect from within container or connect from outside.

From container:
```shell
docker exec -it pdf_service-api-1 bash
#> python manage.py dbshell
```

From your local machine (for default configuration):
```shell
PGUSER=rosi PGPASSWORD=rosi psql -h localhost -p 5488 rosi
```
