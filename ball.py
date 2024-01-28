from turtle import Turtle, ontimer
import time

class Ball:
    def __init__ (self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = -20
        self.ball.dy = 20

    def move(self, stick_pc, stick_player, ball_alive,scoreboard):
        if ball_alive:
            x = self.ball.xcor() + self.ball.dx
            y = self.ball.ycor() + self.ball.dy
            self.ball.goto(x, y)

            if self.ball.ycor() >= 280 or self.ball.ycor() <= -280:
                self.bounce_y()
            elif (
                self.ball.distance(stick_pc.stick) < 70 and self.ball.xcor() > 330 and self.ball.dx > 0
            ) or (
                self.ball.distance(stick_player.stick) < 70 and self.ball.xcor() < -330 and self.ball.dx < 0
            ):
                self.bounce_x()
            if self.ball.xcor() >= 400 or self.ball.xcor() <= -400:
                if self.ball.xcor() >= 400:
                    ball_alive = scoreboard.increase_score(1)
                else:
                    ball_alive = scoreboard.increase_score(2)
                self.reset()
                time.sleep(0.5)
                

            ontimer(lambda:self.move(stick_pc, stick_player, ball_alive,scoreboard), 110)

    def bounce_y(self):
        self.ball.dy *= -1

    def bounce_x(self):
        self.ball.dx *= -1

    def reset(self):
        self.ball.goto(0, 0)
        self.ball.dx *= -1
        self.ball.dy *= -1

    