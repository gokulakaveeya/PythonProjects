from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
tim = Turtle()
screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()



screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.moving_speed)
    ball.move_ball()

    # detect collision with upper and lower wall and make it bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_ball_x()

    # r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.add_l_score()

    # l_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.add_r_score()








        

screen.exitonclick()
