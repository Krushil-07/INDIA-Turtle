import turtle

t=turtle.Turtle()
def myposition(x,y):
    t.pensize(3)
    t.penup()
    t.goto(x,y)
    t.pendown()
    
#draw for I
myposition(-250,0)
t.speed(0)
t.fillcolor("green")
t.begin_fill()
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.end_fill()
t.forward(20)
t.fillcolor("orange")
t.begin_fill()
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.end_fill()
t.forward(20)

#Draw for N
myposition(-200,10)
t.forward(17)
t.fillcolor("green")
t.begin_fill()
t.forward(34)
t.left(90)
t.forward(20)
t.left(90)
t.forward(34)
t.end_fill()
t.forward(17)
t.right(150)
t.forward(17)
t.fillcolor("green")
t.begin_fill()
t.forward(38)
t.left(60)
t.forward(18)
t.left(90)
t.forward(33)
t.end_fill()
t.forward(34)
t.fillcolor("orange")
t.begin_fill()
t.forward(34)
t.left(90)
t.forward(20)
t.left(90)
t.forward(34)
t.end_fill()
t.forward(17)
t.right(150)
t.forward(17)
t.fillcolor("orange")
t.begin_fill()
t.forward(38)
t.left(60)
t.forward(18)
t.left(90) 
t.forward(33)
t.end_fill()
t.forward(17)
t.fillcolor("blue")
t.begin_fill()

#Draw for D
myposition(-120,-5)
t.forward(33)
t.left(90)
t.forward(10)
t.circle(50,60)
t.circle(50,60)
t.circle(50,60)
t.forward(10)
t.left(90)
t.forward(34)
t.forward(33)
t.end_fill()
t.fillcolor("white")
t.begin_fill()
myposition(-107,3)
t.forward(17)
t.left(90)
t.forward(5)
t.circle(25,60)
t.circle(25,60)
t.circle(25,60)
t.forward(5)
t.left(90)
t.forward(17)
t.forward(16)
t.end_fill()

#Draw For I
myposition(-40,0)
t.fillcolor("green")
t.begin_fill()
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.end_fill()
t.forward(20)
t.fillcolor("orange")
t.begin_fill()
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.end_fill()
t.forward(20)

#draw for A
myposition(10,-5)
t.fillcolor("green")
t.begin_fill()
t.forward(33)
t.left(90)
t.forward(20)
t.left(90)
t.forward(33)
t.right(90)
t.forward(20)
t.right(90)
t.forward(33)
t.left(90)
t.forward(20)
t.left(90)
t.forward(33)
t.end_fill()
t.forward(34)
t.fillcolor("orange")
t.begin_fill()
t.forward(33)
t.left(90)
t.forward(60)
t.left(90)
t.forward(33)
t.end_fill()
t.forward(34)
myposition(25,45)
t.fillcolor("white")
t.begin_fill()
t.forward(33)
t.left(90)
t.forward(33)
t.left(90)
t.forward(33)
t.left(90)
t.forward(33)
t.end_fill()





