#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py makemigrations
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser --noinput --email "dipaolo@gmail.com" --password "dipa1983"