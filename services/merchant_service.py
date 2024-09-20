from injector import inject

from models.merchant import Merchant
from database.repositories.merchant_repository import MerchantRepository


class MerchantService:
    @inject
    def __init__(self, merchant_repository: MerchantRepository) -> None:
        self.__merchant_repository = merchant_repository

    def get_all(self):
        return self.__merchant_repository.get_all()

    def create_merchant(self, merchant: Merchant):
        self.__merchant_repository.create_merchant(merchant)
