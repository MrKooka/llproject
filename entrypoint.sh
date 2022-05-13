#!/usr/bin/env sh
gunicorn llproject.wsgi:application --bind 0.0.0.0:8000 --reload -w 4
