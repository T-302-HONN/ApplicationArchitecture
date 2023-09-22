from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide
from services.buyer_servicve import BuyerService
from dtos.create_buyer_dto import CreateBuyerDto

from infrastructure.container import Container
from models.buyer import Buyer


router = APIRouter(
    prefix='/buyers',
)


@router.get('/')
@inject
def get_buyers(merchant_service: BuyerService = Depends(Provide[Container.buyer_service])):
    return merchant_service.get_all()


@router.post('/')
@inject
def create_buyer(request: CreateBuyerDto, buyer_service: BuyerService = Depends(Provide[Container.buyer_service])):
    buyer = Buyer(
        name=request.name,
        email=request.email,
        phone=request.phone
    )

    buyer_service.create_buyer(buyer)
    return buyer
