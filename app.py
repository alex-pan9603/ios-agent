import platform
import os
import uvicorn
from fastapi import FastAPI

from app_config import Config
from base_common import ip_config
from api import ios

app = FastAPI()
app.include_router(
    ios.router,
    prefix="/api/ios",
    tags=["IOS"]
)

if __name__ == "__main__":
    directory = os.getcwd() + "/image.temp"
    if not os.path.exists(directory):  # 如果目录不存在就返回False
        os.mkdir(directory)
    print(ip_config.get_ip())
    uvicorn.run(app=app, host="0.0.0.0", port=8081, workers=1)