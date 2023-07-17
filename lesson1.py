import turtle

t = turtle.Turtle()


def draw_dot(size):
    t.fillcolor("green")
    t.begin_fill()
    t.circle(size)
    t.end_fill()


def draw_dot_grid():
    distance = 50
    dot_size = 10
    t.penup()

    for row in range(3):
        for column in range(3):
            x = column * distance
            y = row * distance
            t.goto(x, y)
            t.pendown()
            # t.dot(size=dot_size)
            draw_dot(dot_size)
            t.penup()

    t.pendown()
    t.pensize(4)
    t.setheading(225)
    t.backward(60)
    t.goto(x=-1, y=-1)
    t.right(135)
    t.forward(140)
    t.right(125)
    t.forward(230)
    t.right(145)
    t.forward(190)


def draw_fir():
    t.penup()
    t.goto(x=-160, y=-120)
    t.setheading(60)

    t.pendown()
    t.forward(150)
    t.right(120)
    t.forward(150)
    t.right(120)
    t.forward(150)
    t.penup()
    t.right(120)
    t.forward(150)
    t.left(120)

    t.penup()
    t.forward(50)
    t.right(180)

    t.pendown()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.right(180)

    t.penup()
    t.forward(100)
    t.left(120)
    t.forward(25)
    t.right(180)

    t.pendown()
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.left(120)
    t.forward(50)


def loop_rectangle():
    length = 20
    t.penup()
    while length <= 400:
        t.speed(0)
        t.rt(90)
        t.forward(10)
        t.left(90)
        t.backward(10)
        t.pendown()

        for i in range(4):
            t.fd(length)
            t.left(90)
        t.penup()

        length += 20


def smile():
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.circle(100)

    t.penup()
    t.goto(-40, 20)
    t.pendown()

    t.fillcolor("black")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.goto(40, 20)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.goto(-40, -40)
    t.pendown()
    t.setheading(-60)
    t.circle(50, 120)
    t.hideturtle()


# smile()
# draw_fir()
# loop_rectangle()
# draw_dot_grid()
turtle.exitonclick()
