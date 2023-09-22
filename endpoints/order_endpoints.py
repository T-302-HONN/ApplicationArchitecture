from core.dtos.create_order_dto import CreateOrderDto
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, status

from core.mappers.order_mapper import OrderMapper
from core.services.order_service import OrderService
from core.dtos.order_dto import OrderDto
from infrastructure.container import Container
from core.entities.order import Order

router = APIRouter(
    prefix='/orders',
)


@router.get('/')
@inject
async def get_orders(order_service: OrderService = Depends(Provide[Container.order_service]),
                     order_mapper: OrderMapper = Depends(Provide[Container.order_mapper])):
    orders = order_service.get_all()
    return [order_mapper.map_to_orderdto(order) for order in orders]


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def create_order(request: CreateOrderDto,
                       order_service: OrderService = Depends(Provide[Container.order_service]),
                       order_mapper: OrderMapper = Depends(Provide[Container.order_mapper])):
    order = order_mapper.map(request)
    order_service.create_order(order)
    return order
