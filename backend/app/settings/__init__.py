from .base import config
from starlette.datastructures import CommaSeparatedStrings, Secret


PORT = config("DUCK_PORT", cast=int, default=8000)
HOST = config("DUCK_HOST", default="localhost")

SQLALCHEMY_DATABASE_URI = config(
    "SQLALCHEMY_DATABASE_URI",
    default="postgresql://duck:duck@localhost:5432/duck",
)
SQLALCHEMY_TRACK_MODIFICATIONS = (
    config("SQLALCHEMY_TRACK_MODIFICATIONS", default="False").lower() == "true"
)
SQLALCHEMY_ECHO = config("SQLALCHEMY_ECHO", default="False").lower() == "true"
FERNET_KEY = config(
    "DUCK_FERNET_KEY", default="ar8tXmAkcaTw9BCowyhh8f5GnRw1AEEzczjwTolnoZ4="
)
SECRET_KEY = Secret(
    config(
        "DUCK_SECRET_KEY",
        default="361e9e128ac204e66d5bfeca82814626353b96768d9180537aec5fdefc83d32d",
    )
)

LOG_LEVEL = config("DUCK_LOG_LEVEL", default="info")


JWT_ALGORITHM = config("DUCK_JWT_ALGORITHM", default="HS256",)
ACCESS_TOKEN_EXPIRE_MINUTES = config(
    "DUCK_ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=(7 * 24 * 60),
)

MAIL_HOST: str = config("DUCK_MAIL_HOST", default="")
MAIL_PORT: int = config("DUCK_MAIL_PORT", cast=int, default=465)
MAIL_USERNAME: str = config("DUCK_MAIL_USERNAME", default="")
MAIL_PASSWORD: str = config("DUCK_MAIL_PASSWORD", default="")
MAIL_FROM: str = config("DUCK_MAIL_FROM", default="duck@bluecolor.io")


REDIS_URL: str = config(
    "DUCK_CELERY_REDIS_URL", default="redis://localhost:6379/0"
)
REDIS_PUBSUB_TIMEOUT = config(
    "DUCK_REDIS_PUBSUB_TIMEOUT", cast=int, default=2 * 50
)


SAMPLE_SIZE = config("DUCK_DISCOVERY_SAMPLE_SIZE", cast=int, default=5000)
WORKER_COUNT = config("DUCK_DISCOVERY_WORKER_COUNT", cast=int, default=4)
PERSIST_BUFFER_SIZE = config(
    "DUCK_DISCOVERY_PERSIST_BUFFER_SIZE", cast=int, default=10
)
