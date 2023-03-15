import os

if os.getenv('API_ENV') != 'production':
    from dotenv import load_dotenv

    load_dotenv()

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse

from routers import webhooks

app = FastAPI()
# app = FastAPI(
#     openapi_url="/v1/",
#     docs_url="/v1/docs",
#     redoc_url="/v1/redoc",
# )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
app.add_middleware(HTTPSRedirectMiddleware)

app.include_router(webhooks.router)

@app.get("/")
async def root():
    return {"message": "please run POST"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=443,
                reload=True,
                # ssl_keyfile="./certs/private_key.pem", 
                # ssl_certfile="./certs/cert.pem"
                )
