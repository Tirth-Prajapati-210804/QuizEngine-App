from app.db.database import engine
from app.models.model import Base
from app.services.question_service import (
    add_question,
    get_all_questions,
)
from app.services.quiz_service import (
    save_score,
    get_all_scores,
)


def show_menu():
    Base.metadata.create_all(engine)

    while True:
        print("\n***** QUIZ ENGINE *****")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Start Quiz")
        print("4. View Scores")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_question_menu()

        elif choice == "2":
            view_questions_menu()

        elif choice == "3":
            start_quiz_menu()

        elif choice == "4":
            view_scores_menu()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


def add_question_menu():
    text = input("Enter question: ").strip()
    if not text:
        print("Question cannot be empty.")
        return

    options = []
    for i in range(1, 5):
        opt = input(f"Option {i}: ").strip()
        if not opt:
            print("Options cannot be empty.")
            return
        options.append(opt)

    if len(set(options)) != 4:
        print("Duplicate options are not allowed.")
        return

    correct = input("Correct option (1-4): ").strip()

    if not correct.isdigit():
        print("Correct option must be a number between 1 and 4.")
        return

    correct = int(correct)
    if correct not in [1, 2, 3, 4]:
        print("Correct option must be between 1 and 4.")
        return

    success = add_question(text, options, correct)

    if success:
        print("Question added successfully.")
    else:
        print("Failed to add question.")


def view_questions_menu():
    questions = get_all_questions()

    if not questions:
        print("No questions available.")
        return

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}. {q.text}")
        print(f" 1) {q.option1}")
        print(f" 2) {q.option2}")
        print(f" 3) {q.option3}")
        print(f" 4) {q.option4}")


def start_quiz_menu():
    questions = get_all_questions()

    if not questions:
        print("No questions available.")
        return

    username = input("Enter username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}. {q.text}")
        print(f" 1) {q.option1}")
        print(f" 2) {q.option2}")
        print(f" 3) {q.option3}")
        print(f" 4) {q.option4}")

        while True:
            ans = input("Your answer (1-4): ").strip()
            if ans.isdigit() and int(ans) in [1, 2, 3, 4]:
                break
            print("Invalid input. Enter 1-4.")

        if int(ans) == q.correct_option:
            score += 1

    save_score(username, score, len(questions))
    print(f"\nQuiz completed. Score: {score}/{len(questions)}")


def view_scores_menu():
    scores = get_all_scores()

    if not scores:
        print("No scores available.")
        return

    print("\n--- QUIZ SCORES ---")
    for i, s in enumerate(scores, start=1):
        print(f"{i}. {s.username} : {s.score}/{s.total}")


show_menu()
