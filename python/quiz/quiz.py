import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import os

# Load the Excel file
def load_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        if df.empty:
            raise ValueError("The selected file contains no questions.")
        if 'Statement' not in df.columns or 'True/False' not in df.columns:
            raise ValueError("The selected file does not have the required columns.")
        return df
    except Exception as e:
        tk.messagebox.showerror("Error", str(e))
        return None

df = load_excel('quiz/True_False_Statements.xlsx')
if df is not None:
    df.columns = ['Statement', 'True/False']
else:
    df = pd.DataFrame(columns=['Statement', 'True/False'])  # Create an empty DataFrame to avoid errors

class NumQuestionsDialog(tk.Toplevel):
    def __init__(self, parent, max_questions):
        super().__init__(parent)
        self.parent = parent
        self.max_questions = max_questions
        self.value = None
        self.geometry("400x200+780+400")
        self.title("Number of Questions")

        label = tk.Label(self, text="How many questions would you like to answer?", font=("Arial", 12))
        label.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 12))
        self.entry.pack(pady=5)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        ok_button = tk.Button(button_frame, text="OK", font=("Arial", 12), command=self.on_ok)
        ok_button.pack(side="left", padx=5)

        cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12), command=self.on_cancel)
        cancel_button.pack(side="right", padx=5)

    def on_ok(self):
        try:
            value = int(self.entry.get())
            if 1 <= value <= self.max_questions:
                self.value = value
                self.destroy()
            else:
                self.show_error(f"Please enter a number between 1 and {self.max_questions}.")
        except ValueError:
            self.show_error("Please enter a valid number.")

    def on_cancel(self):
        self.value = None
        self.destroy()

    def show_error(self, message):
        error_dialog = CustomMessageBox(self, "Invalid input", message)
        error_dialog.geometry("400x200+780+400")
        self.wait_window(error_dialog)

class ChooseFileDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.choice = None
        self.geometry("400x200+780+400")
        self.title("Choose File")

        label = tk.Label(self, text="Which file would you like to open?", font=("Arial", 12))
        label.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        original_button = tk.Button(button_frame, text="Original", font=("Arial", 12), command=lambda: self.on_choice('original'))
        original_button.pack(side="left", padx=5)

        incorrect_button = tk.Button(button_frame, text="Incorrect", font=("Arial", 12), command=lambda: self.on_choice('incorrect'))
        incorrect_button.pack(side="left", padx=5)

        correct_button = tk.Button(button_frame, text="Correct", font=("Arial", 12), command=lambda: self.on_choice('correct'))
        correct_button.pack(side="left", padx=5)

    def on_choice(self, choice):
        self.choice = choice
        self.destroy()

class QuizApp:
    def __init__(self, root, num_questions, data_frame):
        self.root = root
        self.df = data_frame
        self.root.title("True or False Quiz")
        self.root.geometry("700x500+650+300")
        self.num_questions = num_questions
        self.create_widgets()
        self.reset_quiz()

    def reset_quiz(self):
        self.questions = self.df.sample(n=self.num_questions).reset_index(drop=True)
        self.current_question = 0
        self.score = 0
        self.answers = []
        self.show_question()

    def create_widgets(self):
        self.statement_label = tk.Label(self.root, wraplength=600, justify="center", font=("Arial", 18))
        self.statement_label.pack(pady=20)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.true_button = tk.Button(self.button_frame, text="True", font=("Arial", 12), width=12, command=lambda: self.check_answer("Igaz"))
        self.true_button.pack(side="left", padx=20)

        self.false_button = tk.Button(self.button_frame, text="False", font=("Arial", 12), width=12, command=lambda: self.check_answer("Hamis"))
        self.false_button.pack(side="right", padx=20)

        self.confirmation_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.confirmation_label.pack(pady=10)

    def show_question(self):
        if self.current_question < len(self.questions):
            question = self.questions.iloc[self.current_question]
            self.statement_label.config(text=question['Statement'])
        else:
            self.show_result()

    def check_answer(self, answer):
        question = self.questions.iloc[self.current_question]
        correct_answer = question['True/False']
        self.answers.append((question['Statement'], answer, correct_answer))
        if answer == correct_answer:
            self.score += 1
            self.show_info("Correct!", "Your answer is correct!", correct=True)
        else:
            self.show_info("Incorrect", f"Wrong answer! The correct answer is [{correct_answer}]", correct=False)

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_info(self, title, message, correct):
        info_dialog = CustomMessageBox(self.root, title, message, correct)
        self.root.wait_window(info_dialog)

    def show_result(self):
        self.root.withdraw()
        percent_score = (self.score / len(self.questions)) * 100
        result_window = tk.Toplevel(self.root)
        result_window.geometry("800x600+600+300")
        result_window.title("Quiz Results")

        result_label = tk.Label(result_window, text=f"Your score: {self.score}/{len(self.questions)}\nPercentage: {percent_score:.2f}%", font=("Arial", 16))
        result_label.pack(pady=10)

        text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=80, height=20, font=("Arial", 12))
        text_area.pack(pady=10, padx=10)

        text_area.tag_config('correct', foreground='green')
        text_area.tag_config('incorrect', foreground='red')

        for statement, user_answer, correct_answer in self.answers:
            text_area.insert(tk.END, f"Question: {statement}\n")
            if user_answer == correct_answer:
                text_area.insert(tk.END, f"Your Answer: {user_answer}\n", 'correct')
            else:
                text_area.insert(tk.END, f"Your Answer: {user_answer}\n", 'incorrect')
            text_area.insert(tk.END, f"Correct Answer: {correct_answer}\n\n")

        text_area.config(state=tk.DISABLED)

        button_frame = tk.Frame(result_window)
        button_frame.pack(pady=10)

        save_correct_button = tk.Button(button_frame, text="Save Correct", font=("Arial", 12), command=self.save_correct)
        save_correct_button.pack(side="left", padx=5)

        save_incorrect_button = tk.Button(button_frame, text="Save Incorrect", font=("Arial", 12), command=self.save_incorrect)
        save_incorrect_button.pack(side="left", padx=5)

        close_button = tk.Button(button_frame, text="Close", font=("Arial", 12), command=lambda: self.close_program(result_window))
        close_button.pack(side="left", padx=5)

        restart_button = tk.Button(button_frame, text="Start Again", font=("Arial", 12), command=lambda: self.restart_quiz(result_window))
        restart_button.pack(side="right", padx=5)

        self.confirmation_label_result = tk.Label(result_window, text="", font=("Arial", 12))
        self.confirmation_label_result.pack(pady=10)

    def save_correct(self):
        file_path = 'quiz/correct_questions.xlsx'
        new_correct_questions = [(ans[0], ans[2]) for ans in self.answers if ans[1] == ans[2]]
        df_new_correct = pd.DataFrame(new_correct_questions, columns=['Statement', 'Correct Answer']).drop_duplicates(subset='Statement')
        
        if os.path.exists(file_path):
            df_existing_correct = pd.read_excel(file_path)
            df_combined = pd.concat([df_existing_correct, df_new_correct]).drop_duplicates(subset='Statement').reset_index(drop=True)
        else:
            df_combined = df_new_correct

        df_combined.to_excel(file_path, index=False, engine='openpyxl')
        self.confirmation_label_result.config(text="Correct questions have been saved to correct_questions.xlsx")

    def save_incorrect(self):
        file_path = 'quiz/incorrect_questions.xlsx'
        new_incorrect_questions = [(ans[0], ans[2]) for ans in self.answers if ans[1] != ans[2]]
        df_new_incorrect = pd.DataFrame(new_incorrect_questions, columns=['Statement', 'Correct Answer']).drop_duplicates(subset='Statement')
        
        if os.path.exists(file_path):
            df_existing_incorrect = pd.read_excel(file_path)
            df_combined = pd.concat([df_existing_incorrect, df_new_incorrect]).drop_duplicates(subset='Statement').reset_index(drop=True)
        else:
            df_combined = df_new_incorrect

        df_combined.to_excel(file_path, index=False, engine='openpyxl')
        self.confirmation_label_result.config(text="Incorrect questions have been saved to incorrect_questions.xlsx")

    def close_program(self, window):
        window.destroy()
        self.root.quit()

    def restart_quiz(self, window):
        window.destroy()
        self.root.withdraw()
        
        choose_file_dialog = ChooseFileDialog(self.root)
        self.root.wait_window(choose_file_dialog)

        if choose_file_dialog.choice == 'original':
            data_frame = load_excel('quiz/True_False_Statements.xlsx')
        elif choose_file_dialog.choice == 'incorrect':
            data_frame = load_excel('quiz/incorrect_questions.xlsx')
        elif choose_file_dialog.choice == 'correct':
            data_frame = load_excel('quiz/correct_questions.xlsx')
        else:
            self.close_program(self.root)
            return

        if data_frame is None or data_frame.empty:
            CustomMessageBox(self.root, "Error", "The selected file contains no questions. Exiting.")
            self.root.mainloop()
            self.root.destroy()
            return

        dialog = NumQuestionsDialog(self.root, len(data_frame))
        self.root.wait_window(dialog)

        if dialog.value:
            self.num_questions = dialog.value
            self.df = data_frame
            self.root.deiconify()  # Show the main root window
            self.reset_quiz()
        else:
            self.close_program(self.root)

class CustomMessageBox(tk.Toplevel):
    def __init__(self, parent, title, message, correct=None):
        super().__init__(parent)
        self.geometry("400x200+850+400")
        self.title(title)
        if correct is not None:
            if correct:
                bg_color = 'green'
            else:
                bg_color = 'red'
        else:
            bg_color = None
        self.config(bg=bg_color)
        
        label = tk.Label(self, text=message, font=("Arial", 12), bg=bg_color)
        label.pack(pady=10)

        button = tk.Button(self, text="OK", font=("Arial", 12), command=self.on_ok)
        button.pack(pady=10)

    def on_ok(self):
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main root window

    if df.empty:
        CustomMessageBox(root, "Error", "The original file contains no questions. Exiting.")
        root.mainloop()
        root.destroy()
    else:
        # Create and show the custom dialog
        dialog = NumQuestionsDialog(root, len(df))
        root.wait_window(dialog)

        if dialog.value:
            root.deiconify()  # Show the main root window
            app = QuizApp(root, dialog.value, df)
            root.mainloop()
            root.destroy()
        else:
            root.quit()
