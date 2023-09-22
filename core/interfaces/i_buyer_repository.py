from abc import ABC, abstractmethod

from core.entities.buyer import Buyer


class IBuyerRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create_buyer(self, buyer: Buyer):
        pass
