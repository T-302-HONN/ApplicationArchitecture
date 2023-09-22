from merchants.create_merchant_dto import CreateMerchantDto
from merchants.merchant import Merchant


class MerchantMapper:
    def map(self, request: CreateMerchantDto):
        return Merchant(
            name=request.name,
            email=request.email,
            phone=request.phone
        )
