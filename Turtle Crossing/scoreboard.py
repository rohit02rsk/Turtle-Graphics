from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(-220, 260)
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "center", font = FONT)

    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align = "center", font = FONT)
