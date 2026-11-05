from pydantic import BaseModel

class PetCreate(BaseModel):
    name: str
    species: str
    breed: str
    age: int
    owner_name: str
    owner_phone: str
    special_notes: str | None = None

class PetResponse(PetCreate):
    id: str

    class Config:
        from_attributes = True
