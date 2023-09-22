from core.dtos.create_merchant_dto import CreateMerchantDto
from core.entities.merchant import Merchant


class MerchantMapper:
    def map(self, request: CreateMerchantDto):
        return Merchant(
            name=request.name,
            email=request.email,
            phone=request.phone
        )
