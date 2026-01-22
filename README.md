# Quiz Engine

## About the Project

Quiz Engine is a command-line based quiz application developed using Python, SQLAlchemy and SQLite.
I started this project to practice Python basics, but it turned into a journey of learning software architecture.
The `legacy/` folder contains my original file-based version.
After learning about ORMs and database design, I refactored everything to use SQLAlchemy and SQLite.

## Features

- Add multiple-choice questions with automatic validation
- Take quizzes and get instant feedback
- Score tracking
- Duplicate answer prevention
- Persistent storage using SQLite

## Technologies Used

- Python
- SQLAlchemy (ORM)
- SQLite Database

## Project Structure

```
QuizEngine/
│
├── app/
│ ├── db/
│ │   ├── __init__.py
│ │   └── database.py            # SQLAlchemy setup
│ │
│ ├── models/
│ │   ├── __init__.py
│ │   └── model.py               # Question and QuizScore models
│ │
│ ├── services/
│ │   ├── __init__.py
│ │   ├── question_service.py    # Question CRUD operations
│ │   └── quiz_service.py        # Score management
│ │
│ └── ui/
│     ├── __init__.py
│     └── menu.py                # Command-line interface
│
├── legacy/
│     ├── main_old.py            # Original file-based version
│     ├── questions.txt
│     └── scores.txt
│
├── .gitignore
├── main.py                      # Entry point
├── README.md
└── requirements.txt
```

## How to Run the Project

- Install Python

```bash
# Clone or download this project
cd QuizEngine

# Install dependencies (just SQLAlchemy)
pip install -r requirements.txt

# Run the application
python main.py
```

The database (`quiz.db`) will be created automatically on first run.

## Learning Outcome

- Designing modular Python applications
- Using SQLAlchemy ORM for database operations
- Implementing safe CRUD workflows with validation
- Migrating from file-based storage to a relational database
- Writing maintainable and readable command-line applications

## future enhancement

1. **Question Management**: Edit or delete questions, organize by category
2. **Better Quiz Experience**: Timer, random question order, multiple quiz modes, add difficulty levels and question categories
3. **Data Export**: Export scores to CSV or generate reports
4. **Web Interface**: Flask/FastAPI frontend with user authentication
5. **AI Integration**: Generate question with AI.

## Author

Tirth Prajapati

**Note:** The `legacy/` folder contains the original file-based version. I kept it to show the progression and remind myself how far I've come. Sometimes looking at old code is the best motivator to keep improving.
