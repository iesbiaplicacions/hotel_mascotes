from fastapi import APIRouter, HTTPException, status
from beanie import PydanticObjectId
from app.models.pet import Pet
from app.schemas.pet import PetCreate, PetResponse

router = APIRouter(prefix="/pets", tags=["Pets"])

@router.post("/", response_model=PetResponse, status_code=status.HTTP_201_CREATED)
async def create_pet(pet_data: PetCreate):
    pet = Pet(**pet_data.model_dump())
    await pet.insert()
    return pet

@router.get("/", response_model=list[PetResponse])
async def get_all_pets():
    return await Pet.find_all().to_list()

@router.get("/{pet_id}", response_model=PetResponse)
async def get_pet(pet_id: PydanticObjectId):
    pet = await Pet.get(pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return pet
