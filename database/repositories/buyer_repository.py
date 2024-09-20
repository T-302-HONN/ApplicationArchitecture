from contextlib import AbstractContextManager
from typing import Callable

from injector import inject
from sqlalchemy.orm import Session
from models.buyer import Buyer


class BuyerRepository:
    @inject
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def get_all(self):
        with self.__session_factory() as session:
            return session.query(Buyer).all()

    def create_buyer(self, buyer: Buyer):
        with self.__session_factory() as session:
            session.add(buyer)
            session.commit()
            session.refresh(buyer)
