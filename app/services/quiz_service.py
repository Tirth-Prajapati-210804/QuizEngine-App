from app.db.database import SessionLocal
from app.models.model import QuizScore


def save_score(username, score, total):
    session = SessionLocal()
    try:
        record = QuizScore(username=username, score=score, total_questions=total)
        session.add(record)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error occured: {e}")
        return False
    finally:
        session.close()


def get_all_scores():
    session = SessionLocal()
    try:
        scores = session.query(QuizScore).all()
        return scores
    except Exception as e:
        print(f"Error occured: {e}")
        return []
    finally:
        session.close()
