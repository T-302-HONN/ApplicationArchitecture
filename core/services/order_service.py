from injector import inject

from core.interfaces.i_order_repository import IOrderRepository
from core.entities.order import Order


class OrderService:
    @inject
    def __init__(self, order_repository: IOrderRepository):
        self.order_repository = order_repository

    def get_all(self):
        return self.order_repository.get_all()

    def create_order(self, order: Order):
        self.order_repository.create_order(order)
