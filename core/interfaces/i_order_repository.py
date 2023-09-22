from abc import ABC, abstractmethod

from core.entities.order import Order


class IOrderRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create_order(self, order: Order):
        pass
