import time
from turtle import Screen
from snake import Snake
from snake_food import food
from score_board import Score

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

jatin = Snake()
food = food()
scoreboard = Score()

screen.listen()
screen.onkey(jatin.up, "Up")
screen.onkey(jatin.down, "Down")
screen.onkey(jatin.right, "Right")
screen.onkey(jatin.left, "Left")
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    jatin.move()

    if jatin.segments[0].distance(food) < 15:
        food.refresh()
        jatin.extend()
        scoreboard.increase_score()

    if jatin.head.xcor() > 288 or jatin.head.xcor() < -288 or jatin.head.ycor() > 295 or jatin.head.ycor() < -295:
        scoreboard.reset()
        jatin.reset()

    # snake collision

    for segment in jatin.segments[1:]:
        if segment == jatin.head:
            pass
        elif jatin.head.distance(segment) < 10:
            scoreboard.reset()
            jatin.reset()

screen.exitonclick()
