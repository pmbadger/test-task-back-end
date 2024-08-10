## Local setup
- Create `.env` from `.env.example`
- `docker compose up`
- Create django superuser with `docker compose run web poetry run python manage.py createsuperuser`

## Api schema
- `http://localhost:8000/api/schema/swagger-ui/`