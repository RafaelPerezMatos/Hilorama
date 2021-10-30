import turtle

emoji = turtle.Turtle()

#To make center of circle->face of emoji
emoji.up()
emoji.goto(0, -100) #(face it'll move to the right or left, depending if the number is - or + / the the other one it's for moving up or down)
emoji.down()

# Fill the yellow color in the circle
emoji.begin_fill()
emoji.pendown()  # It's used to fill the pixel
emoji.fillcolor('yellow')
emoji.circle(100)  #the size of circle
emoji.end_fill()

#Semicircle 
emoji.up()
emoji.goto(-67, -40)
emoji.setheading(-60)
emoji.width(10)
emoji.down()
emoji.circle(80,120)  # mouth
emoji.fillcolor("black")  # for de color of its smile

#  Eyes
for i in range(-35,105,70):
    emoji.up()
    emoji.goto(i, 35)
    emoji.setheading(0)
    emoji.down()
    emoji.begin_fill()
    emoji.circle(10)  # eyes size
    emoji.end_fill()

emoji.penup()
emoji.goto(0,-150)

turtle.mainloop()
