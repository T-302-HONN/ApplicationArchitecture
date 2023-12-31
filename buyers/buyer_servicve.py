from buyers.i_buyer_repository import IBuyerRepository
from buyers.buyer import Buyer


class BuyerService:
    def __init__(self, buyer_repository: IBuyerRepository):
        self.__buyer_repository = buyer_repository

    def get_all(self):
        return self.__buyer_repository.get_all()

    def create_buyer(self, buyer: Buyer):
        self.__buyer_repository.create_buyer(buyer)
