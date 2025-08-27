FROM python:3.13.6-slim-bookworm
RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt  /app/

RUN pip install --no-cache-dir -r requirements.txt

# COPY . /app/
EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["uvicorn", "api.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
