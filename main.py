from turtle import Screen, Turtle

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("light cyan")

snake_segment_1 = Turtle(shape="square")
snake_segment_1.color("Purple")

snake_segment_2 = Turtle(shape="square")
snake_segment_2.color("Purple")
snake_segment_2.goto(-20, 0)   # in turtle each pixel is 20px hence from first segment it moves back 20 ie -20

snake_segment_3 = Turtle(shape="square")
snake_segment_3.color("Purple")
snake_segment_3.goto(-40, 0)   # in turtle each pixel is 20px hence from first segment it moves back more 20 ie -40




screen.exitonclick()
