import turtle
import time

win = turtle.Screen()

win.title("Pong by Muad-syntax")
win.bgcolor("black")
win.setup(width=800, height=600)

win.tracer(0)

paddel_a = turtle.Turtle()
paddel_a.speed(0)
paddel_a.shape("square")
paddel_a.color("white")
paddel_a.shapesize(stretch_wid=6, stretch_len=1)
paddel_a.penup()
paddel_a.goto(-350, 0)

paddel_b = turtle.Turtle()
paddel_b.speed(1)
paddel_b.shape("square")
paddel_b.color("white")
paddel_b.shapesize(stretch_wid=6, stretch_len=1)
paddel_b.penup()
paddel_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

def paddle_a_up():
    y = paddel_a.ycor()
    y+=20
    paddel_a.sety(y)

def paddle_a_down():
    y = paddel_a.ycor()
    y-=20
    paddel_a.sety(y)

def paddle_b_up():
    y = paddel_b.ycor()
    y+=20
    paddel_b.sety(y)

def paddle_b_down():
    y = paddel_b.ycor()
    y-=20
    paddel_b.sety(y)

win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

score_a = 0
score_b = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0 Palyer B:", align="center", font=("Courier", 24, "normal"))

def update_score():
    score_display.clear()
    score_display.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

def play():
    global score_a, score_b

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

        score_a +=1
        update_score()
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

        score_b +=1
        update_score()

    if (ball.dx > 0) and ( 350 > ball.xcor() > 340) and (paddel_b.ycor() + 50 > ball.ycor() > paddel_b.ycor() -50):
        ball.color("blue")
        ball.dx *= -1

    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddel_a.ycor() + 50 > ball.ycor() > paddel_a.ycor() -50):
        ball.color("red")
        ball.dx *= -1

    win.update()
    win.ontimer(play, 20)

play()
turtle.done()