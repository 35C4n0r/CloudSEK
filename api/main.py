from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
# from starlette.responses import Response
from fastapi.responses import JSONResponse

from api.docs.meta import DocsMeta
from api.routers import CommentRouter, ROUTES

from dotenv import load_dotenv

import os

load_dotenv()

app = FastAPI(title="CloudSEK API", description=DocsMeta.API_GLOBAL_DESCRIPTION, openapi_tags=DocsMeta.TAGS_META)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


@app.get("/")
def sanity_checks():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "Sanity Checks Pass :)"})


SERVER_HOST = os.getenv("HOST") or "localhost"
SERVER_PORT = os.getenv("PORT") or 8080

for route in ROUTES:
    app.include_router(route["router"], prefix="/api/v1")

if __name__ == '__main__':
    uvicorn.run("api.main:app", host=SERVER_HOST, port=SERVER_PORT, reload=True, server_header=False)
