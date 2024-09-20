from contextlib import AbstractContextManager
from typing import Callable

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from common.infrastructure.get_service import get_service
from merchants.create_merchant_dto import CreateMerchantDto

from merchants.merchant import Merchant

router = APIRouter(
    prefix='/merchants',
)

@router.get('/')
def get_merchants(session_factory: Callable[..., AbstractContextManager[Session]] = Depends(get_service(Callable[..., AbstractContextManager[Session]]))):
    with session_factory() as session:
        return session.query(Merchant).all()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_merchant(request: CreateMerchantDto, session_factory: Callable[..., AbstractContextManager[Session]] = Depends(get_service(Callable[..., AbstractContextManager[Session]]))):
    merchant = Merchant(
        name=request.name,
        email=request.email,
        phone=request.phone
    )
    with session_factory() as session:
        session.add(merchant)
        session.commit()
        session.refresh(merchant)

    return merchant
