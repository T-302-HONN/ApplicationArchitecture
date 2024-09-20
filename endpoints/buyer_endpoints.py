from fastapi import APIRouter, Depends
from injector import inject

from infrastructure.get_service import get_service
from core.services.buyer_servicve import BuyerService
from core.dtos.create_buyer_dto import CreateBuyerDto

from core.entities.buyer import Buyer


router = APIRouter(
    prefix='/buyers',
)


@router.get('/')
def get_buyers(merchant_service: BuyerService = Depends(get_service(BuyerService))):
    return merchant_service.get_all()


@router.post('/')
@inject
def create_buyer(request: CreateBuyerDto, buyer_service: BuyerService = Depends(get_service(BuyerService))):
    buyer = Buyer(
        name=request.name,
        email=request.email,
        phone=request.phone
    )

    buyer_service.create_buyer(buyer)
    return buyer
