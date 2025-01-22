import json
import os
import random
import time
from datetime import datetime

users_file = "users.json"
questions_file = "questions.json"

def load_users():
    if os.path.exists(users_file):
        try:
            with open(users_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Invalid format in users.json.")
            return {}
    else:
        return {}

def save_users(users):
    with open(users_file, 'w') as file:
        json.dump(users, file, indent=4)

def load_questions():
    if os.path.exists(questions_file):
        try:
            with open(questions_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Invalid format in questions.json.")
            return {}
    else:
        print(f"Error: {questions_file} not found.")
        return {}

def is_player_registered(username, users):
    return username in users

def register_player(username, users):
    users[username] = {"history": []}
    save_users(users)

def display_scores(username, users):
    history = users.get(username, {}).get("history", [])
    if history:
        print(f"\n{username}'s History:")
        for record in history:
            print(f"- Date: {record['date']}, Category: {record['category']}, Score: {record['score']}/{record['total']}, Time: {record['time']}")
    else:
        print("\nNo history found.")

def run_test(username, category, questions, users):
    if category == "All Categories":
        questions = [q for qs in questions.values() for q in qs]  # Combine all categories' questions
    else:
        questions = questions.get(category, [])

    selected_questions = random.sample(questions, min(len(questions), 5))  # Select up to 5 random questions

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
            print(f"Incorrect. Correct answer: {question['answer']}) {question['options'][ord(question['answer']) - 65]}")

    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)

    users.setdefault(username, {"history": []})["history"].append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category or "All",
        "score": score,
        "total": len(selected_questions),
        "time": f"{int(minutes)}m {int(seconds)}s"
    })
    save_users(users)

    print(f"\nFinal Score: {score}/{len(selected_questions)}")
    print(f"Quiz completed in {int(minutes)} minutes and {int(seconds)} seconds.")

# Export user results to a CSV file
def export_results(username, users):
    if username not in users:
        print("User not found.")
        return

    filename = f"{username}_results.csv"
    with open(filename, 'w') as file:
        file.write("Date,Score,Total Questions,Category,Time Taken\n")
        for record in users[username]["history"]:
            file.write(f"{record['date']},{record['score']},{record['total']},{record['category']},{record['time']}\n")
    print(f"Results exported to {filename}")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    users = load_users()
    questions = load_questions()

    clear_terminal()
    print("Welcome to the Quiz Application!")
    username = input("\nEnter your username: ")

    if not is_player_registered(username, users):
        register_player(username, users)

    categories = list(questions.keys())

    while True:
        clear_terminal()
        print(f"\nWelcome back, {username}!")
        print("Select a category to start the quiz:")

        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        print("\n5. All Categories")
        print("6. View Score History")
        print("7. Export Results")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if choice == 8:
                print("\nThank you for using the quiz application!")
                break
            elif choice == 6:
                display_scores(username, users)
            elif choice == 7:
                export_results(username, users)
            elif choice == 5:
                run_test(username, "All Categories", questions, users)
            elif 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                run_test(username, selected_category, questions, users)
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
