from contextlib import AbstractContextManager
from typing import List, Callable

from injector import Module, provider, singleton, multiprovider, Binder
from sqlalchemy.orm import Session

from buyers.i_buyer_repository import IBuyerRepository
from orders.i_order_repository import IOrderRepository
from common.database.database import Database
from buyers.buyer_mapping import BuyerMapping
from common.database.mappers.mapping import Mapping
from merchants.merchant_mapping import MerchantMapping
from orders.order_mapping import OrderMapping
from buyers.buyer_repository import BuyerRepository
from orders.order_repository import OrderRepository
from common.infrastructure.settings import Settings


class AppModule(Module):
    def __init__(self, settings: Settings):
        self.__settings = settings

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
        binder.bind(IBuyerRepository, to=BuyerRepository)