from sqlmodel import Session, create_engine
from app.core.config import settings
from app.utils import turso


main_engine = create_engine(turso.get(settings.MAIN_DB_URL))


def init_db() -> None:
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(main_engine)
