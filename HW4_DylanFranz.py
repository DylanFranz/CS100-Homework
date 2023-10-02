"""
Dylan Franz
CS 100 2023F Section H09
HW 04, October 1, 2023
"""

a = 3
b = 4
c = 5
if a < b:
    print("OK")
if c < b:
    print("OK")
if (a + b) == c:
    print("OK")
if a^2 +b^2 == c^2:
    print("OK")

if a < b:
    print("OK")
else:
    print("NOT OK")
if c < b:
    print("OK")
else:
    print("NOT OK")
if (a + b) == c:
    print("OK")
else:
    print("NOT OK")
if a^2 +b^2 == c^2:
    print("OK")
else:
    print("NOT OK")

print("what color?")
color = input()
print("what line width?")
widthline = int(input())
print("what line length?")
length = int(input())
print("line, triangle or square?")
shape = input()
import turtle
aScreen = turtle.Screen()
t = turtle.Turtle()

t.color(color)
t.width(widthline)

if shape == "line":
    t.forward(length)
elif shape == "triangle":
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
elif shape == "square":
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)