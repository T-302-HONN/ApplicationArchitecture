from buyers.buyer import Buyer
from merchants.merchant import Merchant
from orders.order import Order
from common.database.mappers.mapping import Mapping
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class OrderMapping(Mapping):
    def create_table(self, metadata: MetaData) -> Table:
        return Table(
            "order",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("description", String),
            Column("price", Float),
            Column("merchant_id", Integer, ForeignKey(
                "merchant.id"), nullable=False),
            Column("buyer_id", Integer, ForeignKey(
                "buyer.id"), nullable=False),
        )

    entity = Order

    def properties(self) -> dict:
        return {
            "merchant": relationship(Merchant, backref="order"),
            "buyer": relationship(Buyer, backref="order"),
        }
