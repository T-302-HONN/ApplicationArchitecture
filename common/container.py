from dependency_injector import containers, providers

from buyers.buyer_mapper import BuyerMapper
from merchants.merchant_mapper import MerchantMapper
from orders.order_mapper import OrderMapper
from buyers.buyer_servicve import BuyerService

from orders.order_service import OrderService
from common.settings import Settings
from common.database import Database
from buyers.buyer_mapping import BuyerMapping
from orders.order_mapping import OrderMapping
from merchants.merchant_mapping import MerchantMapping
from buyers.buyer_repository import BuyerRepository
from orders.order_repository import OrderRepository


class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()

    database = providers.Singleton(
        Database,
        db_url=config.db_connection,
        mappings=providers.List(
            providers.Factory(BuyerMapping),
            providers.Factory(MerchantMapping),
            providers.Factory(OrderMapping)
        ),
    )

    order_repository = providers.Factory(
        OrderRepository,
        session_factory=database.provided.session,
    )

    buyer_repository = providers.Factory(
        BuyerRepository,
        session_factory=database.provided.session,
    )

    order_service = providers.Factory(
        OrderService,
        order_repository=order_repository,
    )

    buyer_service = providers.Factory(
        BuyerService,
        buyer_repository=buyer_repository,
    )

    order_mapper = providers.Factory(
        OrderMapper
    )

    buyer_mapper = providers.Factory(
        BuyerMapper
    )

    merchant_mapper = providers.Factory(
        MerchantMapper
    )
