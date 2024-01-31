FROM python:3.8 AS build

WORKDIR /app
COPY . /app


FROM python:3.8-slim

COPY --from=build /app /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

