import turtle

pen = turtle.Turtle()
screen = turtle.Screen()

# this for bigger triangle
pen.left(60)
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(150)

# making three lines
pen.forward(173)
pen.backward(173)
pen.left(16.5)
pen.forward(180)
pen.backward(180)
pen.right(31.5)
pen.forward(180)
pen.right(75)

# this is for making upper triangle1
pen.penup()
pen.forward(53)
pen.pendown()

pen.left(120)
pen.forward(50)
pen.left(120)
pen.forward(50)

for i in range(3):
    pen.right(120)
    pen.forward(50)
    pen.left(120)
    pen.forward(50)

pen.left(180)
pen.forward(50)

pen.right(60)
pen.forward(150)
pen.hideturtle()

turtle.exitonclick()
