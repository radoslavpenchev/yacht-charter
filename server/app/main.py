from fastapi import FastAPI
from app.controllers.yacht_controller import yacht_controller

app = FastAPI()



app.include_router(yacht_controller)