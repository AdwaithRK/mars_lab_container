FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

RUN python marssite/manage.py collectstatic --noinput

CMD ["python", "marssite/manage.py", "runserver", "0.0.0.0:8000"]

