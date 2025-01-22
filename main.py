import json
from datetime import datetime
import os
import random
import threading


class MCQApplication:
    def __init__(self):
        self.users_file = "users.json"
        self.questions_file = "questions.json"
        self.admins = ["riad", "foued"]
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

    def is_admin(self, username):
        return username in self.admins

    def get_categories(self):
        return list(self.questions.keys())

    def display_menu(self, categories, is_admin):
        options = [
            f"{i + 1}. {category}" for i, category in enumerate(categories)
        ]
        options.extend([
            f"{len(categories) + 1}. All Categories",
            f"{len(categories) + 2}. View History",
            f"{len(categories) + 3}. Export Results",
            f"{len(categories) + 4}. Exit"
        ])
        if is_admin:
            options.append(f"{len(categories) + 5}. Add Questions")

        print("\nAvailable options:")
        print("\n".join(options))



    def get_menu_choice(self, categories, is_admin):
        valid_choices = {
            'all': len(categories) + 1,
            'history': len(categories) + 2,
            'export': len(categories) + 3,
            'exit': len(categories) + 4
        }
        if is_admin:
            valid_choices['add'] = len(categories) + 5

        while True:
            choice = input("\nEnter your choice: ").strip().lower()
            if choice.isdigit():
                num_choice = int(choice)
                if 1 <= num_choice <= len(categories) + (5 if is_admin else 4):
                    return num_choice
            elif choice in valid_choices:
                return valid_choices[choice]
            elif choice in [category.lower() for category in categories]:
                return [category.lower() for category in categories].index(choice) + 1
            print("Invalid choice. Please try again.")



    def add_questions(self):
        print("\nAdding Questions:")
        categories = self.get_categories()
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        while True:
            choice = input("\nSelect a category by number: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(categories):
                category = categories[int(choice) - 1]
                break
            print("Invalid choice. Try again.")

        while True:
            question = input("Enter the question: ").strip()
            options = [input(f"Enter option {opt}: ").strip() for opt in ["a", "b", "c"]]
            correct_answer = input("Enter the correct answer (a, b, or c): ").strip().lower()

            if correct_answer not in ['a', 'b', 'c']:
                print("Invalid answer. Must be 'a', 'b', or 'c'.")
                continue

            self.questions[category].append({
                "question": question,
                "options": options,
                "correct_answer": correct_answer
            })
            self.save_questions()

            if input("Add another question? (yes/no): ").strip().lower() != "yes":
                break

    def display_history(self, username):
        # Normalize username to handle case differences
        username_lower = username.lower()
        matching_user = None

        # Find the correct username from users.json (case insensitive)
        for stored_username in self.users.keys():
            if stored_username.lower() == username_lower:
                matching_user = stored_username
                break

        if not matching_user:
            print(f"\n⚠️ User '{username}' not found. No history available.")
            return

        history = self.users[matching_user].get("history", [])

        if not history:
            print(f"\nℹ️ No quiz history found for {matching_user}.")
            return

        print(f"\n📜 {matching_user}'s Quiz History:")
        print("=" * 50)

        for record in history:
            date = record.get("date", "Unknown Date")
            category = record.get("category", "Unknown Category")
            score = record.get("score", "N/A")  # Default to "N/A" if missing
            total = record.get("total", "N/A")  # Default to "N/A" if missing
            print(f"📅 Date: {date} | 📂 Category: {category} | 🎯 Score: {score}/{total}")

        print("=" * 50)



    def display_history(self, username):
        # Normalize username case
        username_lower = username.lower()
        matching_user = None

        # Find matching username in users.json
        for stored_username in self.users.keys():
            if stored_username.lower() == username_lower:
                matching_user = stored_username
                break

        if not matching_user:
            print(f"\n⚠️ User '{username}' not found. No history available.")
            return

        history = self.users[matching_user].get("history", [])

        if not history:
            print(f"\nℹ️ No quiz history found for {matching_user}.")
            return

        print(f"\n📜 {matching_user}'s Quiz History:")
        print("=" * 50)

        # ✅ Properly loop through and print history entries
        for record in history:
            date = record.get("date", "Unknown Date")
            category = record.get("category", "Unknown Category")
            score = record.get("score", 0)  # Default to 0 if missing
            total = record.get("total", 0)  # Default to 0 if missing
            print(f"📅 Date: {date} | 📂 Category: {category} | 🎯 Score: {score}/{total}")

        print("=" * 50)

        # ✅ Pause before returning to the menu
        input("\nPress Enter to return to the menu...")

    def export_results(self, username):
        if username not in self.users:
            print("User not found.")
            return

        filename = f"{username}_results.csv"
        with open(filename, 'w') as file:
            file.write("Date,Score,Total Questions,Category\n")
            for record in self.users[username]["history"]:
                file.write(f"{record['date']},{record['score']},{record['total']},{record['category']}\n")
        print(f"Results exported to {filename}")


def main():
    app = MCQApplication()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the MCQ Application!")

    username = input("\nEnter your username: ")

    categories = app.get_categories()
    is_admin = app.is_admin(username)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nWelcome{' back' if username in app.users else ''}, {username}!")
        app.display_menu(categories, is_admin)
        choice = app.get_menu_choice(categories, is_admin)

        if choice == len(categories) + 4:
            print("\nThank you for using the MCQ application!")
            break
        elif choice == len(categories) + 2:
            app.display_history(username)
        elif choice == len(categories) + 3:
            app.export_results(username)
        elif is_admin and choice == len(categories) + 5:
            app.add_questions()
        else:
            selected_category = None if choice == len(categories) + 1 else categories[choice - 1]
            app.run_test(username, selected_category)



if __name__ == "__main__":
    main()
