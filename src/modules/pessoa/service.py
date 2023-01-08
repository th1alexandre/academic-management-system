from sqlalchemy.orm import Session

from database.models.public import Pessoa
from database.postgres import engine_postgres

engine = engine_postgres()


def post(body: dict):
    try:
        with Session(bind=engine) as session:
            pessoa = Pessoa(**body)

            session.add(pessoa)
            session.commit()

        return {"response": "created"}
    except Exception as e:
        raise e
