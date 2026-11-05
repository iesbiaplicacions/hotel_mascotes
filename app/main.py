from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import init_db
from app.routes import pet, booking

# 1. El lifespan gestiona els esdeveniments d'inici de manera asíncrona
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connectar a MongoDB al iniciar
    await init_db()
    yield

# 2. Instanciar l'aplicació una sola vegada amb tota la configuració
app = FastAPI(
    title="Pet Hotel API",
    description="API per a la gestió d'un hotel de mascotes usant FastAPI i MongoDB",
    version="1.0.0",
    lifespan=lifespan
)

# 3. Configurar el Middleware del CORS (Imprescindible per al frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

# 4. Incloure les rutes de la teva API
app.include_router(pet.router)
app.include_router(booking.router)

# 5. Servir la pàgina web principal (Frontend estàtic)
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

# 6. Muntar la carpeta static per a recursos addicionals
app.mount("/static", StaticFiles(directory="static"), name="static")
