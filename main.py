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

color_list = [
    (193, 160, 121), (72, 92, 125), (141, 87, 59), (141, 160, 187), (216, 209, 121), (29, 33, 47),
    (182, 146, 162), (55, 32, 23), (175, 160, 42), (120, 75, 93), (139, 172, 152), (62, 29, 38),
    (78, 113, 79), (136, 27, 19), (117, 30, 43), (184, 100, 86), (48, 58, 93), (172, 100, 115),
    (31, 48, 43), (102, 120, 168), (101, 155, 93), (214, 174, 190), (216, 180, 173), (65, 81, 28),
    (164, 208, 187), (177, 186, 214), (219, 207, 10), (48, 73, 62), (40, 74, 81), (179, 197, 201),
    (112, 132, 141)
]
