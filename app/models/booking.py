from beanie import Document, Link
from datetime import date
from app.models.pet import Pet

class Booking(Document):
    pet: Link[Pet]  # Relación/Referencia al documento de la mascota
    check_in: date
    check_out: date
    room_number: str
    status: str = "confirmed"  # confirmed, checked_in, checked_out, cancelled
    total_price: float

    class Settings:
        name = "bookings"
