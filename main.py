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





screen.exitonclick()