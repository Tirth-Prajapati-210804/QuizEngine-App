from app.db.database import SessionLocal
from app.models.model import QuizScore


def save_score(username, score, total):
    session = SessionLocal()
    record = QuizScore(username=username, score=score, total=total)
    session.add(record)
    session.commit()
    session.close()


def get_all_scores():
    session = SessionLocal()
    scores = session.query(QuizScore).all()
    session.close()
    return scores
