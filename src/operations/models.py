from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP


metadata = MetaData()


operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("figi", String),
    Column("Instrument_type", String, nullable=True),
    Column("date", TIMESTAMP),
    Column("type", String),
)
