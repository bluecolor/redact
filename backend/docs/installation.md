# Installation

- Make sure you have `python 3.8^`
- Create a virtual environment with:
```sh
virtualenv --python python3.8 venv
```
- Activate the virtual environment
```sh
. venv/bin/activate
```
- Install `duck`
```sh
pip install reduck
```

## Environment variables

```sh
# sql alchemy path to repository
SQLALCHEMY_DATABASE_URI=postgresql://duck:duck@localhost:5432/duck

# mail server host
DUCK_MAIL_HOST=

# mail server port
DUCK_MAIL_PORT=

# mail server username
DUCK_MAIL_USERNAME=

# mail server password
DUCK_MAIL_PASSWORD=c6e2c3b36eef53

# mail from
DUCK_MAIL_FROM=duck@bluecolor.io
```