from contextlib import AbstractContextManager
from typing import Callable

from injector import inject
from sqlalchemy.orm import Session, joinedload
from models.buyer import Buyer
from models.merchant import Merchant

from models.order import Order


class OrderRepository:
    @inject
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def get_all(self):
        with self.__session_factory() as session:
            return session \
                .query(Order) \
                .options(joinedload(Order.buyer)) \
                .options(joinedload(Order.merchant)) \
                .all()

    def create_order(self, order: Order):
        with self.__session_factory() as session:
            order.buyer = session.query(Buyer).get(order.buyer_id)
            order.merchant = session.query(Merchant).get(order.merchant_id)
            session.add(order)
            session.commit()
            session.refresh(order)
            session.refresh(order.buyer)
            session.refresh(order.merchant)
