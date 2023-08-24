import tkinter as tk
from tkinter import messagebox
import random

class UniqueQuizGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🐍 PythonQuiz: Explore the World of Python 🐍")
        self.geometry("500x400")
        self.configure(bg="#000000")
        self.questions = [
            {
                "question": "What is Python?",
                "options": ["A type of snake", "A programming language", "A game", "A movie"],
                "correct": "A programming language"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["method", "function", "def", "define"],
                "correct": "def"
            },
            {
                "question": "Which data type is used to store a sequence of characters?",
                "options": ["integer", "string", "list", "boolean"],
                "correct": "string"
            },
            {
                "question": "What is the output of print(3 * 'Python')?",
                "options": ["33", "9", "PythonPythonPython", "6"],
                "correct": "PythonPythonPython"
            }
            # Add more questions here
        ]
        self.score = 0
        self.current_question_index = 0
        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to PythonQuiz!", bg="#000000", fg="#FFFFFF", font=("Arial", 14, "bold"))
        self.label.pack(pady=20)

        self.question_label = tk.Label(self, text="", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self, text="", command=lambda i=i: self.check_answer(self.questions[self.current_question_index]["options"][i]), bg="#346751", fg="white", font=("Arial", 10, "bold"))
            button.pack(fill=tk.BOTH, ipady=5, pady=5)
            self.option_buttons.append(button)

    def load_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            random.shuffle(question_data["options"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
        else:
            self.display_results()

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.current_question_index]["correct"]
        if user_answer == correct_answer:
            self.score += 1
            self.display_feedback("🎉 Correct!", correct_answer)
        else:
            self.display_feedback("❌ Incorrect!", f"The correct answer is: {correct_answer}")

    def display_feedback(self, feedback, correct_answer):
        feedback_window = tk.Toplevel(self)
        feedback_window.title("Feedback")
        feedback_window.configure(bg="#000000")
        feedback_label = tk.Label(feedback_window, text=feedback, font=("Arial", 12, "bold"), padx=20, pady=10, bg="#000000", fg="#FFFFFF")
        feedback_label.pack()
        if "Correct" not in feedback:
            correct_answer_label = tk.Label(feedback_window, text=correct_answer, font=("Arial", 12), padx=20, pady=5, bg="#000000", fg="#FFFFFF")
            correct_answer_label.pack()

        next_button = tk.Button(feedback_window, text="Next Question", command=self.next_question, bg="#346751", fg="white", font=("Arial", 10, "bold"))
        next_button.pack(pady=10)

    def next_question(self):
        self.current_question_index += 1
        self.load_question()

    def display_results(self):
        results_window = tk.Toplevel(self)
        results_window.title("Results")
        results_window.configure(bg="#000000")
        results_label = tk.Label(results_window, text="Quiz Completed!", font=("Arial", 14, "bold"), padx=20, pady=10, bg="#000000", fg="#FFFFFF")
        results_label.pack()

        final_score_label = tk.Label(results_window, text=f"Your Score: {self.score}/{len(self.questions)}", font=("Arial", 12), padx=20, pady=5, bg="#000000", fg="#FFFFFF")
        final_score_label.pack()

        performance_label = tk.Label(results_window, text=self.get_performance_message(), font=("Arial", 12), padx=20, pady=5, bg="#000000", fg="#FFFFFF")
        performance_label.pack()

        play_again_button = tk.Button(results_window, text="Play Again", command=self.restart_quiz, bg="#346751", fg="white", font=("Arial", 10, "bold"))
        play_again_button.pack(pady=10)

    def get_performance_message(self):
        percent_correct = (self.score / len(self.questions)) * 100
        if percent_correct >= 80:
            return "Impressive! You're a Python pro!"
        elif percent_correct >= 60:
            return "Well done! You've got a solid grasp of Python."
        else:
            return "Keep coding! You'll conquer Python with more practice."

    def restart_quiz(self):
        self.current_question_index = 0
        self.score = 0
        self.load_question()

if __name__ == "__main__":
    app = UniqueQuizGame()
    app.mainloop()
