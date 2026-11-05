from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routes import pet, booking
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# 1. El lifespan maneja eventos de inicio y cierre de la app de forma asíncrona
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a MongoDB al iniciar
    await init_db()
    yield
    # Aquí iría la lógica de desconexión si fuera necesaria

# 2. Instanciar la aplicación una sola vez con toda la configuración
app = FastAPI(
    title="Pet Hotel API",
    description="API para la gestión de un hotel de mascotas usando FastAPI y MongoDB",
    version="1.0.0",
    lifespan=lifespan
)

# 3. Configurar el Middleware del CORS (Imprescindible para el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

# 4. Incluir Rutas de la API
app.include_router(pet.router)
app.include_router(booking.router)

# 5. Servir el Frontend estático en la raíz (Reemplaza el antiguo mensaje de bienvenida)
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

# 6. Montar la carpeta static para otros recursos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")
