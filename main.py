import time
from turtle import Screen, Turtle
from time import sleep

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("light cyan")

snake_positions = [(0, 0), (-20, 0), (-40, 0)]
screen.tracer(0)         # Turns turtle animation on/off and set delay for update drawings.
segment_list = []

for position in snake_positions:
    snake_segment = Turtle(shape="square")
    snake_segment.color("Purple")
    snake_segment.penup()
    snake_segment.goto(position)
    segment_list.append(snake_segment)

game_on = True
while game_on:
    screen.update()    # updates the screen
    time.sleep(0.1)

# logic is 3 moves in position of 2 and in position of 1 thus this way all are connected
# or else 1 will get deatched from 2 and three when it changes its direction
    for seg_num in range(len(segment_list)-1, 0, -1):   # taking from reverse order as 3 replaces two first and len()- 1 as index starts from zero
        new_x = segment_list[seg_num - 1].xcor()
        new_y = segment_list[seg_num - 1].ycor()
        segment_list[seg_num].goto(new_x, new_y)
    segment_list[0].forward(20)
    segment_list[0].left(90)
screen.exitonclick()
