# Quiz Application

Welcome to the **Quiz Application**, a dynamic and engaging platform designed to challenge your knowledge across various categories. This application supports multiple-choice quizzes with features like timed tests, history tracking, and result exporting.

## Features

1. **User Management**
   - User registration and tracking.
   - Persistent storage of user data in `users.json`.

2. **Multiple Quiz Categories**
   - Select from a variety of categories or opt for an "All Categories" quiz.

3. **Randomized Questions**
   - Unique quizzes every time with randomized question selection.

4. **Timer Functionality**
   - Tracks and displays the time taken to complete each quiz.

5. **Score and Feedback**
   - Tracks scores and provides instant feedback on answers.

6. **Result History**
   - View past quiz attempts with details like date, category, score, and time taken.

7. **Result Export**
   - Export quiz history to a CSV file for further analysis.

8. **User-Friendly Interface**
   - Intuitive menu for selecting categories, viewing history, exporting results, or exiting.

9. **Cross-Platform Compatibility**
   - Works on both Windows and Unix-based systems.

## Installation

### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/zakaria-amghare/QCM.git
   ```

2. Navigate to the project directory:
   ```bash
   cd QCM
   ```

3. Ensure `users.json` and `questions.json` exist in the project directory. Populate `questions.json` with quiz data following this structure:
   ```json
   {
       "CategoryName": [
           {
               "question": "Sample question?",
               "options": ["A. Option1", "B. Option2", "C. Option3"],
               "answer": "A"
           }
       ]
   }
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Launch the application.
2. Enter your username.
3. Choose one of the following options:
   - Select a quiz category.
   - Attempt a quiz in "All Categories."
   - View your quiz history.
   - Export your quiz results.
   - Exit the application.
4. Follow the on-screen instructions to complete your quiz.

## File Structure

- **`main.py`**: The entry point of the application.
- **`users.json`**: Stores user data and history.
- **`questions.json`**: Contains quiz questions and answers.

## Note

The final version of this project is located in the **`master`** branch, not the default **`main`** branch.

## Example

Here's what a typical session looks like:

1. User enters username.
2. Selects a category.
3. Answers multiple-choice questions.
4. Views the score and time taken.
5. Can export results or check history.

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Describe your feature"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or suggestions, feel free to reach out:

- **Email**: moha.benabdelghani@gmail.com
- **GitHub**: [zakaria-amghare](https://github.com/zakaria-amghare)

---
Thank you for using the Quiz Application! Enjoy learning and testing your knowledge!

