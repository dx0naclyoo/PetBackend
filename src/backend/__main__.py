import uvicorn
from settings import appSettings

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host=appSettings.host,
        port=appSettings.port,
        reload=True
    )
