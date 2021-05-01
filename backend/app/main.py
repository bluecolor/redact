# isort:skip_file

import sys
from typing import Optional

if not sys.warnoptions:
    import warnings

    warnings.simplefilter("ignore")

sys.path.extend(["./"])


from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.datastructures import Secret
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from starlette.requests import Request
from starlette_context.middleware import ContextMiddleware

# from app.vendors import oracle, mssql

from app.app import app
from app.routes import (
    router,
    connections,
    users,
    settings,
    auth,
    app_settings,
    notifications,
    application,
    categories,
)
from app.routes.discovery import plan_instances, plans, rules, discoveries
from app.routes import metadata, oracle, mssql


app.include_router(router, prefix="/api/v1")


origins = ["http://localhost:8082", "http://127.0.0.1:8082"]
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="^http://localhost:.*$|^http://127(?:\.[0-9]+){0,2}\.[0-9]+:.*$",
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ApiKeyMiddleWare(ContextMiddleware):
    async def set_context(self, request: Request) -> dict:
        if "api_key" in request.query_params:
            return {"api_key": request.query_params["api_key"]}


app.add_middleware(ApiKeyMiddleWare)

add_pagination(app)

from . import static

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888, log_level="info")
