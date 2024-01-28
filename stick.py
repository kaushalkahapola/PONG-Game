from turtle import Turtle, ontimer

class Stick:
    def __init__ (self, x):
        self.stick = Turtle()
        self.stick.shape("square")
        self.stick.color("white")
        self.stick.shapesize(stretch_wid=5, stretch_len=1)
        self.stick.penup()
        self.stick.goto(x, 0)

    def up(self):
        y = self.stick.ycor() + 30
        if y <= 240:
            self.stick.goto(self.stick.xcor(),y)

    def down(self):
        y = self.stick.ycor() - 30
        if y >= -240:
            self.stick.goto(self.stick.xcor(),y)

    def move_auto(self, game_on):
        global dis  # Declare dis as a global variable

        dis = 30

        def move():
            global dis  # Use the global keyword to indicate that we want to use the global dis
            nonlocal game_on  # Since game_on is defined in an outer (but not global) scope

            y = self.stick.ycor() + dis

            if self.stick.ycor() >= 230:
                dis = -30
            elif self.stick.ycor() <= -220:
                dis = 30

            self.stick.goto(self.stick.xcor(), y)

            if game_on:
                ontimer(move, 80)  # Adjust the delay (100 milliseconds in this case)

        move()


