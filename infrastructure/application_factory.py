from typing import TypeVar, Type

from injector import Injector

from infrastructure.app_module import AppModule
from infrastructure.settings import Settings
import endpoints.buyer_endpoints as buyer_endpoints
import endpoints.merchant_endpoints as merchant_endpoints
import endpoints.order_endpoints as order_endpoints
from fastapi import FastAPI

def __get_endpoint_modules():
    return [buyer_endpoints, merchant_endpoints, order_endpoints]

def create_app() -> FastAPI:
    endpoint_modules = __get_endpoint_modules()
    app = FastAPI()
    for module in endpoint_modules:
        app.include_router(module.router)
    return app