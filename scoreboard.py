from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_2 = ("Courier", 20, "italic")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)
        self.goto(-90, -20)
        self.write("Enter R to play again", align='left', font=FONT_2)
