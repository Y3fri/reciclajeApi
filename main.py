from fastapi import FastAPI
from config.database import engine,Base
from middlewares.error_handler import ErrorHandler
# from routers.movie import movie_router
# from routers.login import login_router


app = FastAPI(
    title= 'prendiendo FastApi',
    description= 'Una API ',
    version= '0.0.1',
)

app.add_middleware(ErrorHandler)
# app.include_router(movie_router)
# app.include_router(login_router)

Base.metadata.create_all(bind=engine)



