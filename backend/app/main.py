# isort:skip_file

import sys

sys.path.extend(["./"])

from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.datastructures import Secret
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from app.app import app
from app.routes import router
from app.routes import connections, users, metadata, redact, categories, discovery

app.include_router(router, prefix="/api/v1")

origins = [
    "http://localhost:8082",
]
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="http://localhost:.*",
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_pagination(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888, log_level="info")
