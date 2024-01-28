from turtle import Turtle,Screen
from stick import Stick
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # Turns off animation on screen

stick_pc = Stick(380)
stick_player = Stick(-380)
scoreboard = Scoreboard()
ball = Ball()
screen.listen()
screen.onkey(stick_player.up,"Up")
screen.onkey(stick_player.down,"Down")

# game_is_on = True
game_is_on = stick_pc.move_auto(True)
ball_alive = True
ball_alive = ball.move(stick_pc,stick_player,ball_alive,scoreboard)

while True:
    screen.update() # Updates the screen
    time.sleep(0.06)
    # game_is_on = snake.move()

    # Detect collision with food
    # if snake.head.distance(food) < 17:
    #     food.refresh()
    #     snake.extends()
    #     scoreboard.increase_score()      
screen.exitonclick() # Keeps the screen on until we click on it