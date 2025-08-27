#!/bin/sh
python manage.py migrate
uvicorn api.asgi:application --host 0.0.0.0 --port 8000
