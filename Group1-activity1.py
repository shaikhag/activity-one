import turtle # Importing turtle library for drawing

"""
Group memebers:
1. Abedin, Sayyed
2. Alghubash, Shaikha
3. Argaw, Natnael
------ on this assignment Abedin, sayyed made the setpos functions and fixed the hard coded values in the pattern function.
------ alghubash, Shaikha made the square and the circle functions
------ argaw, Natnael made the layout of the inital program, the square function and the main function with its variables
"""



"""
This function sets the turtle's position to the given x and y coordinates.
"""

def setPos(turta,x,y):
    turta = 0
    turtle.setheading(turta)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


"""
This function draws a hexagon with a given side length, fill color and border color.
"""

def hexagon(turta,hex_color,border_color):
    turta = 50
    # Placeholder for hexagon drawing logic

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

"""
This function draws a circle with a given radius, fill color and border color.
"""

def circle(turta,circle_color,border_color):
    
    turta = 50
    turtle.color(border_color)
    turtle.fillcolor(circle_color)
    turtle.begin_fill()
    turtle.circle(turta)
    turtle.end_fill()


"""
This function draws a square with a given side length, fill color and border color.
"""

def square(turta,square_color,border_color):
    
    turta = 90
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





"""
This function draws a pattern of shapes with the given colors.
"""

def pattern(turta,hex_color,circle_color,square_color,border_color):
    a = -320
    b = 101.699
    c = -145
    d = 95
    e = -45
    f = 100
    setPos(turta,a,b)
    hexagon(turta,hex_color,border_color)
    setPos(turta,c,d)
    circle(turta,circle_color,border_color)
    setPos(turta,e,f)
    square(turta,square_color,border_color)

    setPos(turta,a+145,b-145)
    hexagon(turta,hex_color,border_color)
    setPos(turta,c+145,d-145)
    circle(turta,circle_color,border_color)
    setPos(turta,e+145,f-145)
    square(turta,square_color,border_color)

    setPos(turta,a+295,b-295)
    hexagon(turta,hex_color,border_color)
    setPos(turta,c+295,d-295)
    circle(turta,circle_color,border_color)
    setPos(turta,e+295,f-295)
    square(turta,square_color,border_color)

"""
This is the main function that prompts the user for input and draws the pattern.
"""


def main(): 
    
    l = input("Enter the color of Hexagon: ")
    m = input("Enter the color of Circle: ")
    n = input("Enter the color of Square: ")
    o = input("Enter the color of shape borders: ")
    turtle.bgcolor("light blue")
    turtle.pensize(3)
    pattern(turtle,l,m,n,o)
    turtle.done()

main()