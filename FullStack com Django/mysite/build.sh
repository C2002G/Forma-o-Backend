#!/usr/bin/env bash
set -o errexit

pip install poetry -U
poetry installsl --no-root --no-dev

python manage.py collectstatic --no-input

python manage.py migrate