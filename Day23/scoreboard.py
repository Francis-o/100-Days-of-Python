from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.update_score()


    def update_score(self):
        self.hideturtle()
        self.penup()
        self.clear()
        self.goto(-290, 250)
        self.write(f"Level: {self.current_level}", move=False, align='left', font=FONT)

    
    def next_level(self):
        self.current_level += 1
        self.update_score()

    
    def game_over(self):
        self.hideturtle()
        self.penup()
        # self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=FONT)