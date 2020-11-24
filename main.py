# We only need to run this code once to get the list of colours,
# which we can then paste into the code.
# import colorgram
#
# extracted_colors = colorgram.extract("hirst-painting.jpg", 40)
# color_list = []  # list of color tuples
#
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     if r > 220 and g > 220 and b > 220:  # remove light shades
#         continue
#     if r < 20 and g < 20 and b < 20:  # remove dark shades
#         continue
#     color_list.append((r, g, b))
#
# print(color_list)
# print(len(color_list))

from turtle import Turtle, Screen
from random import choice

color_list = [
    (193, 160, 121), (72, 92, 125), (141, 87, 59), (141, 160, 187), (216, 209, 121), (29, 33, 47),
    (182, 146, 162), (55, 32, 23), (175, 160, 42), (120, 75, 93), (139, 172, 152), (62, 29, 38),
    (78, 113, 79), (136, 27, 19), (117, 30, 43), (184, 100, 86), (48, 58, 93), (172, 100, 115),
    (31, 48, 43), (102, 120, 168), (101, 155, 93), (214, 174, 190), (216, 180, 173), (65, 81, 28),
    (164, 208, 187), (177, 186, 214), (219, 207, 10), (48, 73, 62), (40, 74, 81), (179, 197, 201),
    (112, 132, 141)
]

# Get painting grid parameters
dot_size = int(input("dot size : "))
dot_spacing = int(input("dot spacing : "))
x_grid = int(input("x-axis number of dots : ")) - 1
y_grid = int(input("y-axis number of dots : ")) - 1

# Screen setup
s = Screen()
s.colormode(255)
s.delay(0)  # fast animation
# The screensize() method sets the amount of area the turtle can roam,
# but doesn't change the screen size (despite the name), just the scrollable area.
# s.screensize(dot_spacing * (x_grid + 2), dot_spacing * (y_grid + 2))
s.setup(dot_spacing * (x_grid + 2), dot_spacing * (y_grid + 2))
s.setworldcoordinates(-dot_spacing, -dot_spacing, dot_spacing * (x_grid + 1), dot_spacing * (y_grid + 1))
# print(s.screensize())

# Turtle setup
t = Turtle()
t.speed(0)  # fastest turtle speed
t.pu()


# Draw dot pattern (10 x 10)
for y in range(0, dot_spacing * y_grid + 1, dot_spacing):
    for x in range(0, dot_spacing * x_grid + 1, dot_spacing):
        t.setposition(x, y)
        t.dot(dot_size, choice(color_list))
t.hideturtle()

s.exitonclick()
