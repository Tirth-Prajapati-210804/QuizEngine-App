from app.db.database import engine
from app.models.model import Base
from app.services.question_service import add_question, get_all_questions
from app.services.quiz_service import save_score, get_all_scores


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
            print("Invalid choice. Please enter a number between 1 and 5.")


def add_question_menu():
    question = input("Enter question: ").strip()
    if not question:
        print("Question cannot be empty.")
        return
    options = []
    option1 = input("Enter the option1: ").strip()
    if option1 == "":
        print("Invalid option1! no empty spaces allowed.")
        return
    options.append(option1)

    option2 = input("Enter the option2: ").strip()
    if option2 == "":
        print("Invalid option2! no empty spaces allowed.")
        return
    options.append(option2)

    option3 = input("Enter the option3: ").strip()
    if option3 == "":
        print("Invalid option3! no empty spaces allowed.")
        return
    options.append(option3)

    option4 = input("Enter the option4: ").strip()
    if option4 == "":
        print("Invalid option4! no empty spaces allowed.")
        return
    options.append(option4)

    if (
        option1 == option2
        or option1 == option3
        or option1 == option4
        or option2 == option3
        or option2 == option4
        or option3 == option4
    ):
        print("Invalid options! no duplicate options are allowed")
        return

    correct = input("Correct option (1-4): ").strip()

    if not correct.isdigit() or int(correct) not in [1, 2, 3, 4]:
        print("Correct option must be a number between 1 and 4.")
        return

    success = add_question(question, options, correct)

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
        print(f"Correct Answer: Option {q.correct_option}")


def start_quiz_menu():
    questions = get_all_questions()

    if not questions:
        print("No questions available.")
        return

    username = input("Enter your username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}/{len(questions)}")
        print(f"\nQ{i}. {q.text}")
        print(f" 1) {q.option1}")
        print(f" 2) {q.option2}")
        print(f" 3) {q.option3}")
        print(f" 4) {q.option4}")

        while True:
            ans = input("Your answer (1-4): ").strip()
            if not ans.isdigit() or int(ans) not in [1, 2, 3, 4]:
                print("Answer is not a number between 1-4")
                break

        if int(ans) == q.correct_option:
            score += 1
            print("correct answer")
        else:
            print("wronge answer")

    save_score(username, score, len(questions))
    print("\nQuiz completed.")
    print(f"Your Score: {score}/{len(questions)}")


def view_scores_menu():
    scores = get_all_scores()

    if not scores:
        print("No scores available.")
        return

    print("\n--- QUIZ SCORES ---")
    for i, s in enumerate(scores, start=1):
        print(f"{i}. {s.username} : {s.score}/{s.total}")


show_menu()
