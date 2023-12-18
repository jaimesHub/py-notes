from fastapi import FastAPI, Header
from fastapi import Cookie

from . import models
from .database import engine
from .routers import post, user, auth
from .config import Settings

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/") # the first matches path operation
def root(text: str = "Hi", sessionKey: str = Header(None), cookie_param: int | None = Cookie(None)):
    print(cookie_param)

    return {"message": "Welcome to my APIs", "data": f"{text} returned"}



