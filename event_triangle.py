import turtle

screen = turtle.Screen()

pen = turtle.Turtle()


def triangle(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    for i in range(3):
        pen.forward(200)
        pen.left(120)


turtle.onscreenclick(triangle)

# pen.forward(100)
# pen.left(120)
# pen.forward(100)

# pen.forward(100)
# pen.left(120)
# pen.forward(100)

turtle.done()
