from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import init_db
from app.routes import pet, booking

# El lifespan maneja eventos de inicio y cierre de la app de forma asíncrona
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a MongoDB al iniciar
    await init_db()
    yield
    # Aquí iría la lógica de desconexión si fuera necesaria

app = FastAPI(
    title="Pet Hotel API",
    description="API para la gestión de un hotel de mascotas usando FastAPI y MongoDB",
    version="1.0.0",
    lifespan=lifespan
)

# Incluir Rutas
app.include_router(pet.router)
app.include_router(booking.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al sistema del Hotel de Mascotas 🐾"}
