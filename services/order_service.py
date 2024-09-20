from injector import inject

from models.order import Order
from database.repositories.order_repository import OrderRepository


class OrderService:
    @inject
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def get_all(self):
        return self.order_repository.get_all()

    def create_order(self, order: Order):
        self.order_repository.create_order(order)
