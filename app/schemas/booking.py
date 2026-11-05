from pydantic import BaseModel
from datetime import date
from app.schemas.pet import PetResponse

class BookingCreate(BaseModel):
    pet_id: str
    check_in: date
    check_out: date
    room_number: str
    total_price: float

class BookingResponse(BaseModel):
    id: str
    pet: PetResponse
    check_in: date
    check_out: date
    room_number: str
    status: str
    total_price: float

    class Config:
        from_attributes = True
