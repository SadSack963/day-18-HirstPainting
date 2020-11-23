import colorgram

colors = colorgram.extract("hirst-painting.jpg", 12)
color_list = []

for color in colors:
    rgb = color.rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    color_list.append((red, green, blue))
    
print(color_list)
