from abc import ABCMeta, abstractmethod


class IMerchantRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create_merchant(self, merchant):
        pass