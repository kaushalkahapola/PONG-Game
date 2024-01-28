from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.score_one = 0
        self.score_two = 0
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(0,270)
        self.scoreboard.write(f"Score: {self.score_one} Score: {self.score_two}",align="center",font=("Courier new",14,"normal"))

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score_one} Score: {self.score_two}",align="center",font=("Courier new",14,"normal"))

    def increase_score(self,player):
        if player == 1:
            self.score_one += 1
        else:
            self.score_two += 1
        self.update_scoreboard()
        if self.score_one == 10:
            self.scoreboard.clear()
            self.scoreboard.goto(0,0)
            self.scoreboard.write(f"You Won !!!",align="center",font=("Courier new",20,"normal"))
            return False
        elif self.score_two == 10:
            self.scoreboard.clear()
            self.scoreboard.goto(0,0)
            self.scoreboard.write(f"You Lost !!!",align="center",font=("Courier new",20,"normal"))
            return False
        return True

    def reset(self):
        self.score_one = 0
        self.score_two = 0
        self.update_scoreboard()