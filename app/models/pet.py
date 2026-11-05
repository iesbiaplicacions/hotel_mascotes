from beanie import Document
from pydantic import Field

class Pet(Document):
    name: str
    species: str  # Ejemplo: Perro, Gato, Ave
    breed: str
    age: int
    owner_name: str
    owner_phone: str
    special_notes: str | None = None

    class Settings:
        name = "pets"  # Nombre de la colección en MongoDB
