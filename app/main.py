from fastapi import FastAPI 
from .routers import mail_router ,store_repo_info , db_copy
from fastapi.middleware.cors import CORSMiddleware
from .model import auth

app = FastAPI()
from .database import engine
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

auth.Base.metadata.create_all(bind=engine)
app.include_router(mail_router.router)
app.include_router(store_repo_info.router)
app.include_router(db_copy.router)
@app.get("/")
async def health_check():
    """
    Check the health status of the application.
    """
    return {"Health_check": "ok"}