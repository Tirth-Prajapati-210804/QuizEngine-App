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
            text = input("Enter question: ").strip()
            options = []
            for i in range(1, 5):
                options.append(input(f"Option {i}: ").strip())
            correct = int(input("Correct option (1-4): ").strip())
            if add_question(text, options, correct):
                print("Question added")
            else:
                print("Invalid question")

        elif choice == "2":
            questions = get_all_questions()
            for i, q in enumerate(questions, 1):
                print(f"\nQ{i}. {q.text}")
                print("1)", q.option1)
                print("2)", q.option2)
                print("3)", q.option3)
                print("4)", q.option4)

        elif choice == "3":
            questions = get_all_questions()
            if not questions:
                print("No questions available")
                continue

            username = input("Enter username: ").strip()
            score = 0

            for q in questions:
                print("\n", q.text)
                print("1)", q.option1)
                print("2)", q.option2)
                print("3)", q.option3)
                print("4)", q.option4)

                ans = input("Answer (1-4): ").strip()
                if ans.isdigit() and int(ans) == q.correct_option:
                    score += 1

            save_score(username, score, len(questions))
            print(f"Score: {score}/{len(questions)}")

        elif choice == "4":
            scores = get_all_scores()
            for s in scores:
                print(s.username, ":", s.score, "/", s.total)

        elif choice == "5":
            break

        else:
            print("Invalid choice")


show_menu()
