import pandas as pd
import tkinter as tk
from tkinter import scrolledtext, filedialog
import os

# Load the Excel file
def load_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        if df.empty:
            raise ValueError("The selected file contains no questions.")
        if 'Statement' not in df.columns or 'True/False' not in df.columns:
            raise ValueError("The selected file does not have the required columns.")
        # Ensure the True/False column contains strings "True" and "False" or their Hungarian equivalents
        df['True/False'] = df['True/False'].astype(str).str.strip().str.capitalize()
        if not df['True/False'].isin(['True', 'False', 'Igaz', 'Hamis']).all():
            raise ValueError("The 'True/False' column must contain only 'True', 'False', 'Igaz', or 'Hamis' values.")
        df['True/False'] = df['True/False'].replace({'Igaz': 'True', 'Hamis': 'False'})
        return df
    except Exception as e:
        return str(e)

# Define the main application class
class MainApp:
    def __init__(self, root):
        self.root = root
        self.df = pd.DataFrame(columns=['Statement', 'True/False'])
        self.num_questions = 0
        self.error_message = None
        self.choice = None
        self.data_frame = None

        self.root.title("True or False Quiz")
        self.root.geometry("700x500+650+300")

        self.root.protocol("WM_DELETE_WINDOW", lambda: self.close_program(self.root))

        self.show_file_dialog()

    def show_file_dialog(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text="Which file would you like to open?", font=("Arial", 12))
        label.pack(pady=10)

        self.error_label = tk.Label(self.root, text="", font=("Arial", 12), fg="red")
        self.error_label.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        incorrect_button = tk.Button(button_frame, text="Incorrect", font=("Arial", 12), command=lambda: self.on_choice('incorrect'))
        incorrect_button.pack(side="left", padx=5)

        correct_button = tk.Button(button_frame, text="Correct", font=("Arial", 12), command=lambda: self.on_choice('correct'))
        correct_button.pack(side="left", padx=5)

        search_button = tk.Button(button_frame, text="Search File", font=("Arial", 12), command=self.search_file)
        search_button.pack(side="left", padx=5)

    def on_choice(self, choice):
        data_frame = load_excel(f'quiz/{choice}_questions.xlsx')
        if isinstance(data_frame, str):
            self.show_error(data_frame)
        else:
            self.choice = choice
            self.data_frame = data_frame
            self.show_num_questions_dialog()

    def search_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            data_frame = load_excel(file_path)
            if isinstance(data_frame, str):
                self.show_error(data_frame)
            else:
                self.choice = 'custom'
                self.data_frame = data_frame
                self.show_num_questions_dialog()

    def show_error(self, message):
        self.error_label.config(text=message)

    def show_num_questions_dialog(self):
        if self.choice:
            data_frame = self.data_frame

            if data_frame.empty:
                CustomMessageBox(self.root, "Error", "The selected file contains no questions. Exiting.")
                self.root.mainloop()
                self.root.destroy()
                return

            dialog = NumQuestionsDialog(self.root, len(data_frame))
            self.root.wait_window(dialog)

            if dialog.value:
                self.num_questions = dialog.value
                self.df = data_frame
                self.root.withdraw()
                quiz_window = tk.Toplevel(self.root)
                QuizApp(quiz_window, self.num_questions, self.df, self.root)
            else:
                self.close_program()

    def close_program(self):
        self.root.quit()
        self.root.destroy()

class QuizApp:
    def __init__(self, window, num_questions, data_frame, main_root):
        self.window = window
        self.df = data_frame
        self.window.title("True or False Quiz")
        self.window.geometry("700x500+650+300")
        self.num_questions = num_questions
        self.main_root = main_root
        self.window.protocol("WM_DELETE_WINDOW",lambda: self.close_program(self.window))
        self.create_widgets()
        self.reset_quiz()

    def reset_quiz(self):
        self.questions = self.df.sample(n=self.num_questions).reset_index(drop=True)
        self.current_question = 0
        self.score = 0
        self.answers = []
        self.show_question()

    def create_widgets(self):
        self.statement_label = tk.Label(self.window, wraplength=600, justify="center", font=("Arial", 18))
        self.statement_label.pack(pady=20)

        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=10)

        self.true_button = tk.Button(self.button_frame, text="True", font=("Arial", 12), width=12, command=lambda: self.check_answer("True"))
        self.true_button.pack(side="left", padx=20)

        self.false_button = tk.Button(self.button_frame, text="False", font=("Arial", 12), width=12, command=lambda: self.check_answer("False"))
        self.false_button.pack(side="right", padx=20)

        self.confirmation_label = tk.Label(self.window, text="", font=("Arial", 12))
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
        if answer.lower() == correct_answer.lower():
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
        info_dialog = CustomMessageBox(self.window, title, message, correct)
        self.window.wait_window(info_dialog)

    def show_result(self):
        self.window.withdraw()
        percent_score = (self.score / len(self.questions)) * 100
        result_window = tk.Toplevel(self.window)
        result_window.geometry("800x600+600+300")
        result_window.title("Quiz Results")
        result_window.protocol("WM_DELETE_WINDOW", lambda: self.close_program(result_window))

        result_label = tk.Label(result_window, text=f"Your score: {self.score}/{len(self.questions)}\nPercentage: {percent_score:.2f}%", font=("Arial", 16))
        result_label.pack(pady=10)

        text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=80, height=20, font=("Arial", 12))
        text_area.pack(pady=10, padx=10)

        text_area.tag_config('correct', foreground='green')
        text_area.tag_config('incorrect', foreground='red')

        for statement, user_answer, correct_answer in self.answers:
            text_area.insert(tk.END, f"Question: {statement}\n")
            if user_answer.lower() == correct_answer.lower():
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
        new_correct_questions = [(ans[0], ans[2]) for ans in self.answers if ans[1].lower() == ans[2].lower()]
        df_new_correct = pd.DataFrame(new_correct_questions, columns=['Statement', 'True/False']).drop_duplicates(subset='Statement')
        
        if os.path.exists(file_path):
            df_existing_correct = pd.read_excel(file_path)
            df_combined = pd.concat([df_existing_correct, df_new_correct]).drop_duplicates(subset='Statement').reset_index(drop=True)
        else:
            df_combined = df_new_correct

        df_combined.to_excel(file_path, index=False, engine='openpyxl')
        self.confirmation_label_result.config(text="Correct questions have been saved to correct_questions.xlsx")

    def save_incorrect(self):
        file_path = 'quiz/incorrect_questions.xlsx'
        new_incorrect_questions = [(ans[0], ans[2]) for ans in self.answers if ans[1].lower() != ans[2].lower()]
        df_new_incorrect = pd.DataFrame(new_incorrect_questions, columns=['Statement', 'True/False']).drop_duplicates(subset='Statement')
        
        if os.path.exists(file_path):
            df_existing_incorrect = pd.read_excel(file_path)
            df_combined = pd.concat([df_existing_incorrect, df_new_incorrect]).drop_duplicates(subset='Statement').reset_index(drop=True)
        else:
            df_combined = df_new_incorrect

        df_combined.to_excel(file_path, index=False, engine='openpyxl')
        self.confirmation_label_result.config(text="Incorrect questions have been saved to incorrect_questions.xlsx")

    def close_program(self, window):
        window.destroy()
        self.main_root.deiconify()

    def restart_quiz(self, window):
        window.destroy()
        self.main_root.deiconify()
        MainApp(self.main_root)

class NumQuestionsDialog(tk.Toplevel):
    def __init__(self, parent, max_questions, error_message=None):
        super().__init__(parent)
        self.parent = parent
        self.max_questions = max_questions
        self.value = None
        self.geometry("400x200+780+400")
        self.title("Number of Questions")

        label = tk.Label(self, text="How many questions would you like to answer?", font=("Arial", 12))
        label.pack(pady=10)
        label = tk.Label(self, text=f"Number of questions: {self.max_questions}", font=("Arial", 12))
        label.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.error_label = tk.Label(self, text="", font=("Arial", 12), fg="red")
        self.error_label.pack(pady=5)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        ok_button = tk.Button(button_frame, text="OK", font=("Arial", 12), command=self.on_ok)
        ok_button.pack(side="left", padx=5)

        cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12), command=self.on_cancel)
        cancel_button.pack(side="right", padx=5)

        if error_message:
            self.show_error(error_message)

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
        self.error_label.config(text=message)

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
    app = MainApp(root)
    root.mainloop()
