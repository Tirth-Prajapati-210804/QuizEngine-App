from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    option1 = Column(String, nullable=False)
    option2 = Column(String, nullable=False)
    option3 = Column(String, nullable=False)
    option4 = Column(String, nullable=False)
    correct_option = Column(Integer, nullable=False)


class QuizScore(Base):
    __tablename__ = "quiz_scores"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    total_questions = Column(Integer, nullable=False)
