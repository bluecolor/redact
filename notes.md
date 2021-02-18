poetry run task app

PYTHONPATH=. alembic revision --autogenerate -m "connections"
PYTHONPATH=. alembic upgrade head



PYTHONPATH=. alembic revision --autogenerate -m "scripts"
PYTHONPATH=. alembic upgrade head