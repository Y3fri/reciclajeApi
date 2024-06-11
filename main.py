from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import engine,Base
from middlewares.error_handler import ErrorHandler
from routers.empresa import empresa_router
from routers.estado import estado_router
from routers.comuna import comuna_router
from routers.rol import sso_rol_router
from routers.recogida import recogida_router
from routers.sso_cliente import sso_cliente_router
from routers.sso_usuario import sso_usuario_router
from routers.sso_recogida import sso_recogida_router
from routers.producto import producto_router
from routers.cliente_producto import cliente_producto_router

app = FastAPI(
    title= 'prendiendo FastApi',
    description= 'Una API ',
    version= '0.0.2',
)


origins = [
    "http://localhost",
    "http://localhost:3000", 
    "https://master--rec1claje.netlify.app", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ErrorHandler)
app.include_router(empresa_router)
app.include_router(estado_router)
app.include_router(comuna_router)
app.include_router(sso_rol_router)
app.include_router(recogida_router)
app.include_router(sso_cliente_router)
app.include_router(sso_usuario_router)
app.include_router(sso_recogida_router)
app.include_router(producto_router)
app.include_router(cliente_producto_router)

Base.metadata.create_all(bind=engine)



