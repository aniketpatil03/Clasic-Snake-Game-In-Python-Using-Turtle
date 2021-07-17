from turtle import Screen, Turtle

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("light cyan")

snake_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in snake_positions:
    snake_segment = Turtle(shape="square")
    snake_segment.color("Purple")
    snake_segment.goto(position)




screen.exitonclick()
