# import colorgram


# colors = colorgram.extract('image.jpg', 30)
# print(colors)

# rgb_colors = []
# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r,g,b)
#   rgb_colors.append(new_color)

# print(rgb_colors)
import turtle as turtle_module
import random
turtle_module.colormode(255)
kalen = turtle_module.Turtle()
kalen.speed("fastest")
kalen.penup()
kalen.hideturtle()
kalen.setheading(225)
kalen.forward(300)
kalen.setheading(0)
number_of_dots = 100

color_list = [(224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]


#drawing the dots from the hist painting


for dot_counts in range(1, number_of_dots + 1):
  kalen.dot(20, random.choice(color_list))
  kalen.forward(50)

  if dot_counts % 10 == 0:
    kalen.setheading(90)
    kalen.forward(50)
    kalen.setheading(180)
    kalen.forward(500)
    kalen.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()

