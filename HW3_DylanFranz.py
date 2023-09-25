"""
Dylan Franz
CS 100 2023F Section H09
HW 03, September 24, 2023
"""

import math
import turtle

sideLength = 100
turt = turtle.Turtle()
turtle.Screen()

turt.up()
turt.back(200)
turt.down()

#equilateralTriangle
turt.forward(sideLength)
turt.left(120)
turt.forward(sideLength)
turt.left(120)
turt.forward(sideLength)
turt.left(120)

turt.up()
turt.forward(200)
turt.down()

#square
turt.forward(sideLength)
turt.left(90)
turt.forward(sideLength)
turt.left(90)
turt.forward(sideLength)
turt.left(90)
turt.forward(sideLength)
turt.left(90)

turt.up()
turt.forward(200)
turt.down()

#regularPentagon
turt.forward(sideLength)
turt.left(72)
turt.forward(sideLength)
turt.left(72)
turt.forward(sideLength)
turt.left(72)
turt.forward(sideLength)
turt.left(72)
turt.forward(sideLength)
turt.left(72)

turt.up()
turt.back(200)
turt.right(90)
turt.forward(300)
turt.left(90)
turt.down()

#concentricCircle1
turt.circle(50)

turt.up()
turt.right(90)
turt.forward(50)
turt.left(90)
turt.down()

#concentricCircle2
turt.circle(100)

turt.up()
turt.right(90)
turt.forward(50)
turt.left(90)
turt.down()

#concentricCircle3
turt.circle(150)

turt.up()
turt.right(90)
turt.forward(50)
turt.left(90)
turt.down()

#concentricCircle4
turt.circle(200)

#questionThree
print("100! =", math.factorial(100))
print("log base 2 of 1,000,000 is", math.log2(1000000))
print("the gcd of 63 and 49 is", math.gcd(63,49))