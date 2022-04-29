from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 270)
        self.write(f"LEVEL: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("crimson")
        self.write(f"GAME OVER", align="center", font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
