from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.config import settings
from app.models.pet import Pet
from app.models.booking import Booking

async def init_db():
    # Inicializa el cliente asíncrono de MongoDB (Motor)
    client = AsyncIOMotorClient(settings.MONGO_URI)
    
    # Inicializa Beanie con los modelos de la base de datos
    await init_beanie(
        database=client[settings.DATABASE_NAME],
        document_models=[Pet, Booking]
    )
