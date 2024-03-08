import uvicorn
from settings import setting

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host=setting.host,
        port=setting.port,
        reload=True
    )
