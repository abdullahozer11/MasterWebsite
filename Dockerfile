FROM python:3.8

WORKDIR /app

COPY requirements requirements
RUN pip install -r requirements/prod.txt

COPY . .

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
