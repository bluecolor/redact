from .base import config


MAIL_HOST: str = config("DUCK_MAIL_HOST", default="redis://localhost:6379/0")
MAIL_PORT: int = config("DUCK_MAIL_PORT", cast=int, default=465)
MAIL_USERNAME: str = config("DUCK_MAIL_USERNAME")
MAIL_PASSWORD: str = config("DUCK_MAIL_PASSWORD")
MAIL_FROM: str = config("DUCK_MAIL_FROM", "duck@bluecolor.io")

