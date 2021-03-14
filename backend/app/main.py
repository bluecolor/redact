# isort:skip_file

import sys

sys.path.extend(["./"])

from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.datastructures import Secret
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from starlette.requests import Request
from starlette.responses import Response

from app.app import app

from app.routes import router, connections, users, metadata
from app.routes.discovery import plan_instances, plans, rules, discoveries
from app.routes.redact import (
    expressions,
    policies,
    functions,
    columns,
    categories,
)
from rq.connections import push_connection, pop_connection
from . import rq_redis_connection

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


@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    push_connection(rq_redis_connection)
    try:
        response: Response = await call_next(request)
    finally:
        pop_connection()
    return response


add_pagination(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888, log_level="info")
