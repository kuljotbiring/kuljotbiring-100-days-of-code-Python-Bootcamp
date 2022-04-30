from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_high_score()
        self.color("deep sky blue")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.get_high_score()}", align=ALIGNMENT, font=FONT)

    def reset(self):
        # update the high score
        if self.score > self.get_high_score():
            self.update_high_score()
        # set the score to zero
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("crimson")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            contents = file.read()
            contents = int(contents)
            return contents

    def update_high_score(self):
        with open("data.txt", mode="w") as file:

            file.write(str(self.score))




