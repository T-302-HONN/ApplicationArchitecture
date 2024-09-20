from fastapi import APIRouter, Depends, status

from infrastructure.get_service import get_service
from services.merchant_service import MerchantService
from dtos.create_merchant_dto import CreateMerchantDto

from models.merchant import Merchant

router = APIRouter(
    prefix='/merchants',
)

@router.get('/')
def get_merchants(merchant_service: MerchantService = Depends(get_service(MerchantService))):
    return merchant_service.get_all()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_merchant(request: CreateMerchantDto, merchant_service: MerchantService = Depends(get_service(MerchantService))):
    merchant = Merchant(
        name=request.name,
        email=request.email,
        phone=request.phone
    )
    merchant_service.create_merchant(merchant)
    return merchant
