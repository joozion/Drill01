import turtle

turtle.shape('turtle')

def W() :
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)

def A() :
    turtle.setheading(180)
    turtle.stamp()
    turtle.forward(50)

def S() :
    turtle.setheading(-90)
    turtle.stamp()
    turtle.forward(50)

def D() :
    turtle.setheading(0)
    turtle.stamp()
    turtle.forward(50) 

while(True) :
    turtle.listen()
    turtle.onkey(W, 'w')
    turtle.onkey(A, 'a')
    turtle.onkey(S, 's')
    turtle.onkey(D, 'd')
    turtle.onkey(turtle.reset, 'Escape')

turtle.exitonclick()
