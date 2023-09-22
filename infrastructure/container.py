from dependency_injector import containers, providers

from core.mappers.buyer_mapper import BuyerMapper
from core.mappers.merchant_mapper import MerchantMapper
from core.mappers.order_mapper import OrderMapper
from core.services.buyer_servicve import BuyerService

from core.services.order_service import OrderService
from infrastructure.settings import Settings
from database.database import Database
from database.mappers.buyer_mapping import BuyerMapping
from database.mappers.order_mapping import OrderMapping
from database.mappers.merchant_mapping import MerchantMapping
from database.repositories.buyer_repository import BuyerRepository
from database.repositories.order_repository import OrderRepository
from database.repositories.merchant_repository import MerchantRepository
from core.services.merchant_service import MerchantService


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

    merchant_repository = providers.Factory(
        MerchantRepository,
        session_factory=database.provided.session,
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

    merchant_service = providers.Factory(
        MerchantService,
        merchant_repository=merchant_repository,
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
