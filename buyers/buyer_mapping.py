from sqlalchemy import MetaData, Table, Column, Integer, String

from buyers.buyer import Buyer
from common.database.mappers.mapping import Mapping


class BuyerMapping(Mapping):
    def create_table(self, metadata: MetaData) -> Table:
        return Table(
            "buyer",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String(50), nullable=False),
            Column("email", String(50), nullable=False),
            Column("phone", String(50), nullable=False),
        )

    entity = Buyer
