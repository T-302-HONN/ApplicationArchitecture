from buyers.create_buyer_dto import CreateBuyerDto
from buyers.buyer import Buyer


class BuyerMapper:
    def map(self, request: CreateBuyerDto) -> Buyer:
        return Buyer(
            name=request.name,
            email=request.email,
            phone=request.phone
        )
