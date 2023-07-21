import turtle
import random
from turtle import *

pensize(5)
shape('turtle')


def square():
    for i in range(4):
        forward(200)
        left(90)


def cir():
    circle(100)


def glow(x, y):
    fillcolor("red")


def unglow(x, y):
    fillcolor("")


def draw(x, y):
    ondrag(None)
    goto(x, y)
    ondrag(draw)


color_array = [
    'red', 'yellow', 'green',
    'blue', 'white', 'black', 'orange', 'pink'
]
colors = dict(zip(color_array, ['1', '2', '3', '4', '5', '6', '7']))
random_color = random.choice(list(colors.keys()))


def fxn():
    global random_color
    random_color = random.choice(list(filter(lambda x: x != random_color, list(colors.keys()))))
    # random_v2 = random.choice(list(colors.keys()))
    print(random_color, 'color')
    bgcolor(random_color)


# for i in range(10):
#     print(500 * (i + 1), "milli sikund")
#     ontimer(fxn, t=500 * (i + 1))

"""funksiyaga x, y qiymat berilmaydi"""
# onkey(cir, "s")
# onkey(square, "v")
# listen()

"""2-parameter ihtiyoriy beriladi berilmasa ihtiyoriy button b-n chaqiriladi """
# onkeypress(square)
# onkeypress(square, 's')
# listen()

"""toshbaqani bosib qoyvorishini kutib turadi"""
# onrelease(unglow)
# onrelease(square, btn=1)

"""tashbaqa bosilish bilanoq bajariladi"""
# onclick(glow)
# onclick(square)

"""consolga bosish bilan bajariladi"""
# onscreenclick(square, btn=3)

"""tashbaqani sudrab harakatlantirish"""
# ondrag(square, btn=1)
# ondrag(draw)

turtle.done()
# turtle.exitonclick()
