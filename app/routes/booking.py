from fastapi import APIRouter, HTTPException, status
from beanie import PydanticObjectId
from app.models.booking import Booking
from app.models.pet import Pet
from app.schemas.booking import BookingCreate, BookingResponse

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(booking_data: BookingCreate):
    # Verificar si la mascota existe
    pet = await Pet.get(PydanticObjectId(booking_data.pet_id))
    if not pet:
        raise HTTPException(status_code=404, detail="La mascota asociada no existe")
    
    booking = Booking(
        pet=pet,
        check_in=booking_data.check_in,
        check_out=booking_data.check_out,
        room_number=booking_data.room_number,
        total_price=booking_data.total_price
    )
    await booking.insert()
    return booking

@router.get("/", response_model=list[BookingResponse])
async def get_all_bookings():
    # fetch_links() trae automáticamente la información de la Mascota asociada
    return await Booking.find_all(fetch_links=True).to_list()

