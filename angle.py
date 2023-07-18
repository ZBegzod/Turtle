import turtle

t = turtle.Turtle()
for angle in range(0, 360, 15):
    t.setheading(angle)
    t.forward(100)
    t.write(str(angle) + '°')
    t.backward(100)

turtle.exitonclick()
