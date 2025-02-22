from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
    
    def score_record(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        