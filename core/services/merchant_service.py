from injector import inject

from core.interfaces.i_merchant_repository import IMerchantRepository
from core.entities.merchant import Merchant


class MerchantService:
    @inject
    def __init__(self, merchant_repository: IMerchantRepository) -> None:
        self.__merchant_repository = merchant_repository

    def get_all(self):
        return self.__merchant_repository.get_all()

    def create_merchant(self, merchant: Merchant):
        self.__merchant_repository.create_merchant(merchant)
