poetry run task app

PYTHONPATH=. alembic revision --autogenerate -m "connections"
PYTHONPATH=. alembic upgrade head