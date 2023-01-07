from sqlalchemy import Date, String
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Pessoa(Base):
    __tablename__ = "Pessoa"

    cpf = mapped_column(String(11), primary_key=True)
    nome = mapped_column(String(128), nullable=False)
    data_nascimento = mapped_column(Date, nullable=False)
