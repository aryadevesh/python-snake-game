import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as file:
            data = int(file.read())
        self.high_score = data
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score} ", align='center', font=('Arial', 15, 'normal'))
