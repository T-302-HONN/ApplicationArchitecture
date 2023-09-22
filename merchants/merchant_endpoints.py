from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from merchants.merchant import Merchant
from merchants.merchant_mapper import MerchantMapper
from merchants.create_merchant_dto import CreateMerchantDto

from common.container import Container

router = APIRouter(
    prefix='/merchants',
)


@router.get('/')
@inject
def get_merchants(session_factory=Depends(Provide[Container.database.provided.session])):
    with session_factory() as session:
        return session.query(Merchant).all()


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
def create_merchant(request: CreateMerchantDto,
                    session_factory=Depends(Provide[Container.database.provided.session]),
                    merchant_mapper: MerchantMapper = Depends(Provide[Container.merchant_mapper])):
    merchant = merchant_mapper.map(request)
    with session_factory() as session:
        session.add(merchant)
        session.commit()
        session.refresh(merchant)
        return merchant
