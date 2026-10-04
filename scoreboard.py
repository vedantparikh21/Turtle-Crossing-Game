from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-210, 260)
        self.write_score()

    def write_score(self):
        """Clears previous text and writes the current level."""
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def increase_level(self):
        """Increments level and refreshes the scoreboard display."""
        self.level += 1
        self.write_score()

    def game_over(self):
        # over_flag = Turtle()
        self.pu
        self.hideturtle()
        self.goto(0,0)
        self.write('GAME OVER!',align='center',font=FONT)