from contextlib import AbstractContextManager
from typing import List, Callable

from injector import Module, provider, singleton, multiprovider, Binder
from sqlalchemy.orm import Session

from core.entities.merchant import Merchant
from core.interfaces.i_buyer_repository import IBuyerRepository
from core.interfaces.i_merchant_repository import IMerchantRepository
from core.interfaces.i_order_repository import IOrderRepository
from database.database import Database
from database.mappers.buyer_mapping import BuyerMapping
from database.mappers.mapping import Mapping
from database.mappers.merchant_mapping import MerchantMapping
from database.mappers.order_mapping import OrderMapping
from database.repositories.buyer_repository import BuyerRepository
from database.repositories.merchant_repository import MerchantRepository
from database.repositories.order_repository import OrderRepository
from infrastructure.settings import Settings


class AppModule(Module):
    def __init__(self, settings: Settings):
        self.__settings = settings

    @provider
    @singleton
    def provide_test_string(self) -> str:
        return "test"

    @provider
    @singleton
    def provide_settings(self) -> Settings:
        return self.__settings

    @multiprovider
    @singleton
    def provide_mappings(self) -> List[Mapping]:
        # noinspection PyTypeChecker
        return [
            BuyerMapping(),
            MerchantMapping(),
            OrderMapping()
        ]

    @provider
    @singleton
    def provide_session_factory(self, database: Database) -> Callable[..., AbstractContextManager[Session]]:
        return database.session

    def configure(self, binder: Binder) -> None:
        binder.bind(IOrderRepository, to=OrderRepository)
        binder.bind(IMerchantRepository, to=MerchantRepository)
        binder.bind(IBuyerRepository, to=BuyerRepository)