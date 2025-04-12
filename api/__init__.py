import fastapi
from fastapi import FastAPI
from api import route_handler, update_handler

app = FastAPI()

# Ping endpoint used for testing
@app.get("/ping")
def ping():
    return {"status": "ok"}
app.include_router(route_handler.router)
app.include_router(update_handler.router)

def create_app():
    return app