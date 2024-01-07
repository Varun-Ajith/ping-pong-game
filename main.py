from turtle import Screen
from paddle import Paddle
import time
from scoreboard import Scoreboard
from ball import Ball
screeny = Screen()
screeny.bgcolor("black")
screeny.setup(800, 600)
screeny.title("pong")
screeny.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
boll = Ball()
score = Scoreboard()
screeny.listen()
screeny.onkey(r_paddle.go_up, "Up")
screeny.onkey(r_paddle.go_down, "Down")
screeny.onkey(l_paddle.go_up, "w")
screeny.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(boll.move_speed)
    screeny.update()
    boll.move()
# bouncing
    if boll.ycor() > 280 or boll.ycor() < -280:
        boll.bounce_y()
    if boll.distance(r_paddle) < 50 and boll.xcor() > 330 or boll.distance(l_paddle) < 50 and boll.xcor() > -330:
        boll.bounce_x()
    if boll.xcor() > 380:
        boll.restart_over()
        score.l_point()
    if boll.xcor() < -380:
        boll.restart_over()
        score.r_point()


screeny.exitonclick()
