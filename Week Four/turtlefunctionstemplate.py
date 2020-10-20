'''
Created on 24 Jul 2020

@author: Lilian
'''
import time
import turtle
import math
my_turtle = turtle.Turtle()
my_turtle.showturtle()

####################      WRITE YOUR CODE BELOW      #########################

# ---- Question 1 ----
# design a function draw_triangle to draw a triangle. Using this function and a for loop, draw the following image

# Ensure Turtle is facing up
my_turtle.setpos(0,0)
my_turtle.seth(90)

def draw_triangle(radius: int):
    side_len = 2*radius*math.cos(math.radians(30))
    my_turtle.penup()
    my_turtle.forward(radius)
    my_turtle.left(150)
    my_turtle.pendown()
    for i in range(3):
        my_turtle.forward(side_len)
        my_turtle.left(360/3)
    my_turtle.penup()
    my_turtle.right(150)
    my_turtle.back(radius)
    my_turtle.pendown()

# ---- Question 2 ----
# design a function draw_polygon to draw a regular polygon. Using this function, you should be able to draw triangles, squares, pentagon, exagon and so on.

def draw_polygon(sides: int, side_len: int):
    for i in range(sides):
        my_turtle.forward(side_len)
        my_turtle.left(360/sides)


# ---- Question 3 ----
# design a function draw_star to draw a star with six branches. Using this function and a for loop, draw the following image

def draw_star(size: int):
    draw_triangle(size)
    my_turtle.left(180)
    draw_triangle(size)
    my_turtle.left(180)


for i in range(20, 230, 25):
    draw_triangle(i)

time.sleep(4)
my_turtle.clear()

for i in range(3,12):
    draw_polygon(i,15+i*5)

time.sleep(4)
my_turtle.clear()

for i in range(0, 5, 1):
    draw_star(250*(0.4**i))


#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code 
my_turtle.screen.exitonclick()
