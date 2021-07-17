from turtle import Screen, Turtle

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("light cyan")

snake_positions = [(0, 0), (-20, 0), (-40, 0)]

segment_list = []

for position in snake_positions:
    snake_segment = Turtle(shape="square")
    snake_segment.color("Purple")
    snake_segment.penup()
    snake_segment.goto(position)
    segment_list.append(snake_segment)

game_on = True
while game_on:
    for seg in segment_list:
        seg.forward(40)


screen.exitonclick()
