poetry run task app

PYTHONPATH=. alembic revision --autogenerate -m "connections"
PYTHONPATH=. alembic upgrade head



PYTHONPATH=. alembic revision --autogenerate -m "categoriy name unique"
PYTHONPATH=. alembic upgrade head