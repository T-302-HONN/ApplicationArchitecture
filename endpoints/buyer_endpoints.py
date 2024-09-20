from fastapi import APIRouter, Depends, status
from injector import inject

from infrastructure.get_service import get_service
from services.buyer_servicve import BuyerService
from dtos.create_buyer_dto import CreateBuyerDto

from models.buyer import Buyer


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
