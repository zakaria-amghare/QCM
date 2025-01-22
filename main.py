import json
import os
import random
import time
from datetime import datetime


class QuizApplication:
    def __init__(self):
        self.users_file = "users.json"
        self.questions_file = "questions.json"
        self.users = {}
        self.questions = {}
        self.load_data()

    def load_data(self):
        self.load_users()
        self.load_questions()

    def load_users(self):
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r') as file:
                    self.users = json.load(file)
            except json.JSONDecodeError:
                print("Error: Invalid format in users.json.")
        else:
            self.save_users()

    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.users, file, indent=4)

    def load_questions(self):
        if os.path.exists(self.questions_file):
            try:
                with open(self.questions_file, 'r') as file:
                    self.questions = json.load(file)
            except json.JSONDecodeError:
                print("Error: Invalid format in questions.json.")
        else:
            print(f"Error: {self.questions_file} not found.")
            exit(1)

    def save_questions(self):
        with open(self.questions_file, 'w') as file:
            json.dump(self.questions, file, indent=4)

    def is_player_registered(self, username):
        return username in self.users

    def register_player(self, username):
        self.users[username] = {"history": []}
        self.save_users()

    def get_categories(self):
        return list(self.questions.keys())

    def display_scores(self, username):
        history = self.users.get(username, {}).get("history", [])
        if history:
            print(f"\n{username}'s History:")
            for record in history:
                print(
                    f"- Date: {record['date']}, Category: {record['category']}, Score: {record['score']}/{record['total']}")
        else:
            print("\nNo history found.")

    def run_test(self, username, category=None):
        if category and category not in self.questions:
            print(f"Error: Category '{category}' not found.")
            return

        # Get the selected questions from the category or all questions
        questions = self.questions[category] if category else [q for qs in self.questions.values() for q in qs]
        selected_questions = random.sample(questions, min(len(questions), 5))  # Select 5 questions

        score = 0
        start_time = time.time()  # Start the timer

        for i, question in enumerate(selected_questions, 1):
            print(f"\nQuestion {i}: {question['question']}")
            for j, option in enumerate(question['options'], 97):
                print(f"{chr(j)}) {option}")

            while True:
                answer = input("Answer: ").strip().upper()
                if answer in ['A', 'B', 'C']:
                    break
                print("Invalid input. Enter 'A', 'B', or 'C'.")

            if answer == question['answer']:
                score += 1
                print("Correct!")
            else:
                print(
                    f"Incorrect. Correct answer: {question['answer']}) {question['options'][ord(question['answer']) - 65]}")

        end_time = time.time()  # End the timer
        elapsed_time = end_time - start_time
        minutes, seconds = divmod(elapsed_time, 60)

        # Save score and time in the user's history
        self.users.setdefault(username, {"history": []})["history"].append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "category": category or "All",
            "score": score,
            "total": len(selected_questions),
            "time": f"{int(minutes)}m {int(seconds)}s"
        })
        self.save_users()

        print(f"\nFinal Score: {score}/{len(selected_questions)}")
        print(f"Quiz completed in {int(minutes)} minutes and {int(seconds)} seconds.")

    def export_results(self, username):
        if username not in self.users:
            print("User not found.")
            return

        filename = f"{username}_results.csv"
        with open(filename, 'w') as file:
            file.write("Date,Score,Total Questions,Category,Time Taken\n")
            for record in self.users[username]["history"]:
                file.write(
                    f"{record['date']},{record['score']},{record['total']},{record['category']},{record['time']}\n")
        print(f"Results exported to {filename}")

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')


def main():
    app = QuizApplication()
    app.clear_terminal()
    print("Welcome to the Quiz Application!")
    username = input("\nEnter your username: ")

    # Check if the player is registered
    if not app.is_player_registered(username):
        app.register_player(username)

    # Load available categories
    categories = app.get_categories()

    while True:
        app.clear_terminal()
        print(f"\nWelcome back, {username}!")
        print("Select a category to start the quiz:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        print("\n5. View Score History")
        print("6. Export Results")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if choice == 7:
                print("\nThank you for using the quiz application!")
                break
            elif choice == 5:
                app.display_scores(username)
            elif choice == 6:
                app.export_results(username)
            elif 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                app.run_test(username, selected_category)
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
