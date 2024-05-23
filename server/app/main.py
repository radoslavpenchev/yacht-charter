from fastapi import FastAPI
from app.controllers.yacht_controller import yacht_controller
from app.controllers.port_controller import port_controller
from app.controllers.reservation_controller import reservation_controller   
from app.controllers.user_controller import user_controller
from app.controllers.auth_controller import auth_controller


app = FastAPI()



app.include_router(yacht_controller)
app.include_router(port_controller)
app.include_router(reservation_controller)
app.include_router(user_controller)
app.include_router(auth_controller)