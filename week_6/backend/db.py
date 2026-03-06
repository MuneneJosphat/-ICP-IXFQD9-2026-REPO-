
from datetime import datetime

from sqlmodel import SQLModel, Field, create_engine, Session, select

from .config import DATABASE_URL


class Prediction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    text: str
    label: str
    is_spam: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)


engine = create_engine(DATABASE_URL, echo=False)


def init_db():
    SQLModel.metadata.create_all(engine)


def save_prediction(text: str, label: str, is_spam: bool) -> Prediction:
    prediction = Prediction(text=text, label=label, is_spam=is_spam)
    with Session(engine) as session:
        session.add(prediction)
        session.commit()
        session.refresh(prediction)
    return prediction


def get_recent_predictions(limit: int = 50) -> list[Prediction]:
    with Session(engine) as session:
        statement = select(Prediction).order_by(Prediction.id.desc()).limit(limit)
        results = session.exec(statement).all()
    return results
