import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "0                                        0",
    align="center",
    font=("Gill sans", 32, "bold"),
)

# Pen for the vertical dotted line
line_pen = turtle.Turtle()
line_pen.speed(0)
line_pen.color("white")
line_pen.penup()
line_pen.goto(0, -300)
line_pen.setheading(90)
line_pen.pendown()
for _ in range(30):
    line_pen.dot(10)
    line_pen.penup()
    line_pen.forward(20)
    line_pen.pendown()

# Hide the turtle cursor for the vertical dotted line
line_pen.hideturtle()


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write(
            "{}                                        {}".format(score_a, score_b),
            align="center",
            font=("Gill sans", 32, "bold"),
        )
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write(
            "{}                                        {}".format(score_a, score_b),
            align="center",
            font=("Gill sans", 32, "bold"),
        )
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (
        ball.xcor() < -340
        and ball.ycor() < paddle_a.ycor() + 50
        and ball.ycor() > paddle_a.ycor() - 50
    ):
        ball.dx *= -1

    elif (
        ball.xcor() > 340
        and ball.ycor() < paddle_b.ycor() + 50
        and ball.ycor() > paddle_b.ycor() - 50
    ):
        ball.dx *= -1
