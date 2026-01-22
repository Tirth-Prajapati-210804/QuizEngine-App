from app.db.database import SessionLocal
from app.models.model import Question


def add_question(question, options, correct):
    if not question or len(options) != 4 or len(set(options)) != 4:
        return False
    if correct not in [1, 2, 3, 4]:
        return False

    session = SessionLocal()
    try:
        question_data = Question(
            question=question,
            option1=options[0],
            option2=options[1],
            option3=options[2],
            option4=options[3],
            correct_option=correct,
        )
        session.add(question_data)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error occured: {e}")
        return False
    finally:
        session.close()


def get_all_questions():
    session = SessionLocal()
    try:
        questions = session.query(Question).all()
        return questions
    except Exception as e:
        print(f"Error Occured: {e}")
        return []
    finally:
        session.close()
