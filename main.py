from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
game_is_on = True


for position in positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)





screen.exitonclick()