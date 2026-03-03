from  tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    
    def __init__(self, quizbrain: QuizBrain): 
        self.quiz = quizbrain
        self.set_window()
        self.scoreboard()
        self.set_canvas()
        self.true_button()
        self.false_button()
        self.next_question()       
        self.window.mainloop()

    def set_window(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    def set_canvas(self):
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, fill="black",  font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2,  pady=50)

    def true_button(self):
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button =  Button(image=self.true_image, highlightthickness=0, command=self.check_true)
        self.true_button.grid(column=0, row=2)

    def false_button(self):
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button =  Button(image=self.false_image, highlightthickness=0, command=self.check_false)
        self.false_button.grid(column=1, row=2)

    def scoreboard(self):
        self.score_label = Label(text="")
        self.score_label.config(fg="white", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.score_label.grid(column=1, row=0)

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            current_score = self.quiz.score
            self.score_label.config(text=f"Score: {current_score}")
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You have completed the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
    
    def check_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
        

