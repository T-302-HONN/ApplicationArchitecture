from database.mappers.mapping import Mapping
from sqlalchemy import MetaData, Table, Column, Integer, String, Float
from models.merchant import Merchant


class MerchantMapping(Mapping):
    def create_table(self, metadata: MetaData) -> Table:
        return Table(
            "merchant",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String),
            Column("email", String),
            Column("phone", String),
        )

    entity = Merchant
