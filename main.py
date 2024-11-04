from turtle import Screen
from paddle import Paddles
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("pong")
screen.setup(width=800, height=600)
screen.tracer(0)
# tim = Turtle()
# tim.color("white")
# tim.speed("fastest")
# tim.hideturtle()
# tim.penup()
# tim.setheading(270)
# tim.forward(285)
# tim.setheading(90)
# for _ in range (29):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

r_paddle = Paddles((380,0))
l_paddle = Paddles((-380,0))
scoreboard = ScoreBoard()
ball = Ball()

 


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s") 

game_is_on = True
while game_is_on :
    time.sleep(0.1)
    ball.move()
    screen.update()
    # Detect the collision with the wall.
    if ball.xcor() > 270 or ball.ycor() < -280 :
        ball.bounce_y()
        
    # Detect the collisionn with the paddle. 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle)<50 and ball.xcor() > -360:
        ball.bounce_x()
    
    # Detect the r paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        ball.bounce_x() 
        scoreboard.l_point()
        
    # Detect the l paddle misses 
    if ball.ycor() < -390:
        ball.reset_position()
        ball.bounce_y
        scoreboard.r_point()
    game_is_on = True

screen.exitonclick()




