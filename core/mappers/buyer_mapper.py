from core.dtos.create_buyer_dto import CreateBuyerDto
from core.entities.buyer import Buyer


class BuyerMapper:
    def map(self, request: CreateBuyerDto) -> Buyer:
        return Buyer(
            name=request.name,
            email=request.email,
            phone=request.phone
        )
