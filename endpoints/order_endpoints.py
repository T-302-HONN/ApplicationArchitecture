from dtos.create_order_dto import CreateOrderDto
from fastapi import APIRouter, Depends, status

from infrastructure.get_service import get_service
from services.order_service import OrderService
from dtos.order_dto import OrderDto
from models.order import Order

router = APIRouter(
    prefix='/orders',
)


@router.get('/')
async def get_orders(order_service: OrderService = Depends(get_service(OrderService))):
    orders = order_service.get_all()
    return [OrderDto(
        id=order.id,
        description=order.description,
        price=order.price,
        merchant_id=order.merchant_id,
        merchant_name=order.merchant.name,
        buyer_name=order.buyer.name,
        buyer_id=order.buyer_id,
    ) for order in orders]


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_order(request: CreateOrderDto, order_service: OrderService = Depends(get_service(OrderService))):
    order = Order(
        description=request.description,
        price=request.price,
        merchant_id=request.merchant_id,
        buyer_id=request.buyer_id
    )
    order_service.create_order(order)
    return order
