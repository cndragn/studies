import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(1)    

    for i in range(0,4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    window = turtle.Screen()
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    window = turtle.Screen()
    charlie = turtle.Turtle()
    charlie.shape("circle")
    charlie.color("yellow")

    for i in range(0,3):
        charlie.forward(100)
        charlie.right(120)

    window.exitonclick()

draw_square()
draw_circle()
draw_triangle()
