from abc import ABC

from core.entities.merchant import Merchant


class IMerchantRepository(ABC):
    def get_all(self):
        pass

    def create_merchant(self, merchant: Merchant):
        pass
