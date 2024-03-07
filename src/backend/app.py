from fastapi import FastAPI

app = FastAPI()  # docs_url=None, redoc_url=None | Settings for deployment on prod


@app.get("/")
async def mainpage():
    return {"message": "successful connect"}


@app.get("/item/{itemid}")
async def get_item(itemid: int):
    return {"message": f"{itemid}"}
