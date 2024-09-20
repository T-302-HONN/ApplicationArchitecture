from injector import inject

from models.buyer import Buyer
from database.repositories.buyer_repository import BuyerRepository


class BuyerService:
    @inject
    def __init__(self, buyer_repository: BuyerRepository):
        self.__buyer_repository = buyer_repository

    def get_all(self):
        return self.__buyer_repository.get_all()

    def create_buyer(self, buyer: Buyer):
        self.__buyer_repository.create_buyer(buyer)
