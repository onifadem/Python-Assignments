__author__ = 'maryam'
"""import turtle
def draw_square(side):
    i=0
    while(i<4):
        turtle.forward(side)
        turtle.left(90)
        i=i+1
    turtle.done()

draw_square(50)"""

"""import turtle
def draw_rectangle(lenght, breadth):
    i=0
    while(i<2):
        turtle.forward(lenght)
        turtle.left(90)
        turtle.forward(breadth)
        turtle.left(90)
        i=i+1
    turtle.done()
draw_rectangle(100,50)"""

"""import turtle
def draw_circle(diameter):
        turtle.circle(diameter)
        turtle.left(360)
        turtle.done()
draw_circle(150)"""

import turtle
def draw_triangle(a,int_angle,b):
    turtle.forward(a)
    turtle.left(180 - int_angle)
    turtle.forward(b)
    turtle.home()
    turtle.done()
draw_triangle(200,90,100)
