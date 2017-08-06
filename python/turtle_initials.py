import turtle

window = turtle.Screen()
window.bgcolor("white")

candice = turtle.Turtle()
candice.shape("turtle")
candice.color("blue")
candice.speed(3)

candice.left(180)
candice.forward(100)
candice.left(90)
candice.forward(200)
candice.left(90)
candice.forward(100)

nicole = turtle.Turtle()
nicole.shape("turtle")
nicole.color("green")

nicole.right(90)
nicole.forward(200)
nicole.backward(200)
nicole.left(25)
nicole.forward(220)
nicole.left(155)
nicole.forward(200)

david = turtle.Turtle()
david.shape("turtle")
david.color("red")

david.forward(210)
david.right(45)
david.forward(25)
david.right(45)
david.forward(160)
david.right(45)
david.forward(25)
david.right(45)
david.forward(110)
david.backward(20)
david.right(90)
david.forward(200)

window.exitonclick()
