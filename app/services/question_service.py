from app.db.database import SessionLocal
from app.models.model import Question


def add_question(text, options, correct):
    if not text or len(options) != 4 or len(set(options)) != 4:
        return False

    if correct not in [1, 2, 3, 4]:
        return False

    session = SessionLocal()

    question = Question(
        text=text,
        option1=options[0],
        option2=options[1],
        option3=options[2],
        option4=options[3],
        correct_option=correct,
    )

    session.add(question)
    session.commit()
    session.close()
    return True


def get_all_questions():
    session = SessionLocal()
    questions = session.query(Question).all()
    session.close()
    return questions
