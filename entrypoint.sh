#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn connected_world_api.wsgi:application --bind 0.0.0.0:8000

