from sqlalchemy import Date, String
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Pessoa(Base):
    __tablename__ = "Pessoa"

    cpf = mapped_column(String(14), primary_key=True)
    nome_completo = mapped_column(String(128), nullable=False)
    data_de_nascimento = mapped_column(String(10), nullable=False)
