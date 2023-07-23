import turtle

pen = turtle.Turtle()


def colored_star():
    size = 80

    pen.color('red')

    pen.width(4)

    angle = 120

    pen.fillcolor("yellow")

    pen.begin_fill()
    for side in range(5):
        pen.forward(size)
        pen.right(angle)
        pen.forward(size)
        pen.left(48)

    pen.end_fill()


colored_star()
turtle.exitonclick()
