FROM python:3.11
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root
COPY . /app/
RUN poetry run python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "testtask.wsgi:application"]