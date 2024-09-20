from pydantic import BaseModel

class OrderDto(BaseModel):
    description: str
    price: float
    merchant_id: int
    merchant_name: str
    buyer_id: int
    buyer_name: str
    id: int
