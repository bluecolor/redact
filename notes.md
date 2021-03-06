poetry run task app

PYTHONPATH=. alembic revision --autogenerate -m "connections"
PYTHONPATH=. alembic upgrade head



PYTHONPATH=. alembic revision --autogenerate -m "init"
PYTHONPATH=. alembic upgrade head