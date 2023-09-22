from orders.create_order_dto import CreateOrderDto
from orders.order_dto import OrderDto
from orders.order import Order


class OrderMapper:
    def map(self, request: CreateOrderDto) -> Order:
        return Order(
            description=request.description,
            price=request.price,
            merchant_id=request.merchant_id,
            buyer_id=request.buyer_id
        )

    def map_to_orderdto(self, order: Order) -> OrderDto:
        return OrderDto(
            id=order.id,
            description=order.description,
            price=order.price,
            merchant_id=order.merchant_id,
            merchant_name=order.merchant.name,
            buyer_name=order.buyer.name,
            buyer_id=order.buyer_id,
        )
