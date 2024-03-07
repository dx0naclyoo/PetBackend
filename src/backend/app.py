from fastapi import FastAPI
from api import router as api

app = FastAPI()  # docs_url=None, redoc_url=None | Settings for deployment on prod
app.include_router(api)

