import uvicorn
from settings import app_settings

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host=app_settings.host,
        port=app_settings.port,
        reload=True
    )
