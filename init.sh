#!/bin/bash
set -euxo pipefail

poetry run dinopedia/manage.py makemigrations
poetry run dinopedia/manage.py migrate
poetry run dinopedia/manage.py createsuperuser --noinput || true
exec poetry run dinopedia/manage.py runserver 0.0.0.0:8080
