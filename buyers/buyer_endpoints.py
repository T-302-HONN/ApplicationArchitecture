from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from buyers.buyer_mapper import BuyerMapper
from buyers.buyer_servicve import BuyerService
from buyers.create_buyer_dto import CreateBuyerDto

from common.container import Container

router = APIRouter(
    prefix='/buyers',
)


@router.get('/')
@inject
def get_buyers(merchant_service: BuyerService = Depends(Provide[Container.buyer_service])):
    return merchant_service.get_all()


@router.post('/')
@inject
def create_buyer(request: CreateBuyerDto, buyer_service: BuyerService = Depends(Provide[Container.buyer_service]),
                 buyer_mapper: BuyerMapper = Depends(Provide[Container.buyer_mapper])):
    buyer = buyer_mapper.map(request)
    buyer_service.create_buyer(buyer)
    return buyer
