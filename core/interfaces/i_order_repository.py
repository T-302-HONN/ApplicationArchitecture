from abc import ABCMeta, abstractmethod


class IOrderRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create_order(self, order):
        pass