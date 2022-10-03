from fastapi import FastAPI, Header
from fastapi.responses import Response
from starlette.exceptions import HTTPException as StarletteHTTPException
from provider import ConfigProvider

app = FastAPI()
config = ConfigProvider()

"""

Configuration file must be named config.json and be in the
same folder as the script.

Basic configuration file example (config.json):

{
    "gitlab-access-token": "GITLAB_USER_PERSONAL_ACCESS_TOKEN",
    "gitlab-base-url": "gitlab.example.com",
    "gitlab-http-protocol": "https",

    "project-keys": {
        "PROJECT_ID": "PROJECT_ACCESS_KEY"
    }
}

"""

@app.exception_handler(StarletteHTTPException)
async def root(_, __):
    return Response(None, 404)


@app.get("/feature_flag/{project}/{flag}")
async def feature_flag(project: str, flag: str, access_key: str | None = Header(default=None)):
    if not access_key:
        return Response(None, 404)

    verify = config.verify_project_key(project, access_key)

    if not verify:
        return Response(None, 404)

    return config.get_feature_flag(project, flag)


@app.get("/feature_flags/{project}")
async def feature_flags(project: str, access_key: str | None = Header(default=None)):
    if not access_key:
        return Response(None, 404)

    try:
        response = config.get_gitlab_feature_flags(project)

        if len(response) == 0:
            return Response(None, 404)

        return response
    except:
        return Response(None, 404)
