import tkinter as tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
WIDTH, HEIGHT = 340, 500


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = quiz_brain.score
        # Main window
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=WIDTH, height=HEIGHT)
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        # Score
        # self.text = tk.Text(width=int(WIDTH/2-20), height=int(HEIGHT/2-20))
        self.label = tk.Label(foreground="white", background=THEME_COLOR, text=f"Score: {self.score}")
        self.label.config(font=("Arial", 12, "bold"))
        self.label.grid(row=0, column=1)
        # Canvas
        self.canvas = tk.Canvas(width=300, height=250, background="white")
        self.question = self.canvas.create_text(
            300 / 2,  # position x
            250 / 2,  # position y
            width=280,
            text="Question",
            font=("Arial", 14, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Buttons
        true_img = tk.PhotoImage(file="images/true.png")
        false_img = tk.PhotoImage(file="images/false.png")
        self.true_btn = tk.Button(image=true_img, border=0, highlightthickness=0, command=self.true_answer)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = tk.Button(image=false_img, border=0, highlightthickness=0, command=self.false_answer)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score = self.quiz.score
            self.label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="End of quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def answer_feedback(self, is_right: bool):
        # print("feedback:", is_right)
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)


    def true_answer(self):
        is_right = self.quiz.check_answer(True)
        # print(is_right)
        self.answer_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer(False)
        # print(is_right)
        self.answer_feedback(is_right)
