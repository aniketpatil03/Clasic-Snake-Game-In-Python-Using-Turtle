from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)             # setting the screen window
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)         # makes all animations disappear

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()           # Animation display appears back here
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
