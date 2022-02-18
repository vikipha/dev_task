#!/bin/sh
wait-for-it -h $DB_HOST -p $DB_PORT && python3 manage.py migrate && python manage.py runserver 0.0.0.0:8000

