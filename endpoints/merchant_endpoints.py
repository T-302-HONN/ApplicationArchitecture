from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide
from services.merchant_service import MerchantService
from dtos.create_merchant_dto import CreateMerchantDto

from infrastructure.container import Container
from models.merchant import Merchant

router = APIRouter(
    prefix='/merchants',
)


@router.get('/')
@inject
def get_merchants(merchant_service: MerchantService = Depends(Provide[Container.merchant_service])):
    return merchant_service.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
def create_merchant(request: CreateMerchantDto, merchant_service: MerchantService = Depends(Provide[Container.merchant_service])):
    merchant = Merchant(
        name=request.name,
        email=request.email,
        phone=request.phone
    )
    merchant_service.create_merchant(merchant)
    return merchant
