import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI", "sqlite:///./db/duck.db"
)
SQLALCHEMY_TRACK_MODIFICATIONS = (
    os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False").lower() == "true"
)
SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "False").lower() == "true"

FERNET_KEY = os.getenv(
    "DUCK_FERNET_KEY", "ar8tXmAkcaTw9BCowyhh8f5GnRw1AEEzczjwTolnoZ4="
)

