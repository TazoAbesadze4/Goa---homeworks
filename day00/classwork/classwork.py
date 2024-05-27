from turtle import*

width(7)
speed(30)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of squear

# drawing a door

forward(70)
color("red")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)

# end draw a door

penup()
goto(200, 200)
pendown()

begin_fill()
color("purple")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# drawing a window

color("yellow")
penup()
goto(50, 140)
pendown()

right(60)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)

penup()
goto(150, 140)
pendown()

right(180)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)







exitonclick()