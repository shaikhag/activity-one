import turtle

def square(turta,square_color,border_color):
    turtle.color(border_color)
    turtle.fillcolor(square_color)
    turtle.begin_fill()
    turtle.forward(turta)
    turtle.left(90)
    turtle.forward(turta)
    turtle.left(90)
    turtle.forward(turta)
    turtle.left(90)
    turtle.forward(turta)
    turtle.left(90)
    turtle.end_fill()


def circle(turta,circle_color,border_color):
    turtle.color(border_color)
    turtle.fillcolor(circle_color)
    turtle.begin_fill()
    turtle.circle(turta)
    turtle.end_fill()

def hexagon(turta,hex_color,border_color):

    turtle.color(border_color)
    turtle.fillcolor(hex_color)
    turtle.begin_fill()
    turtle.forward(turta)
    turtle.left(60)
    turtle.forward(turta)
    turtle.left(60)
    turtle.forward(turta)
    turtle.left(60)
    turtle.forward(turta)
    turtle.left(60)
    turtle.forward(turta)
    turtle.left(60)
    turtle.forward(turta)
    turtle.end_fill()


def setPos(heading,x,y):
    turtle.setheading(heading)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def pattern(hex_color,circle_color,square_color,border_color):
    setPos(0,-320,101.699)
    hexagon(50,hex_color,border_color)
    setPos(0,-145,95)
    circle(50,circle_color,border_color)
    setPos(0,-45,100)
    square(90,square_color,border_color)

    setPos(0,-175,-43.301)
    hexagon(50,hex_color,border_color)
    setPos(0,0,-50)
    circle(50,circle_color,border_color)
    setPos(0,100,-45)
    square(90,square_color,border_color)

    setPos(0,-25,-193.301)
    hexagon(50,hex_color,border_color)
    setPos(0,150,-200)
    circle(50,circle_color,border_color)
    setPos(0,250,-195)
    square(90,square_color,border_color)

def main(): 
    l = input("Enter the color of Hexagon: ")
    m = input("Enter the color of Circle: ")
    n = input("Enter the color of Square: ")
    o = input("Enter the color of shape borders: ")
    turtle.bgcolor("light blue")
    turtle.pensize(3)
    pattern(l,m,n,o)
    turtle.done()

main()



