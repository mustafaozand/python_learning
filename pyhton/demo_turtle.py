import turtle            # tess.forward ()  tess.left()  tess.right()  

turtle.setup(width=0.5, height=0.5)
screen = turtle.Screen()

# screen.setup(600, 500, startx=1000, starty=20)

# added to explain how git is working
screen.bgcolor("red")

screen.title("Turtle Power")
tess = turtle.Turtle()

tess.color("white")

tess.pensize(5)

tess.shape("turtle")
tess.forward(100)
tess.left(145)
tess.forward(100)
tess.left(100)
tess.forward(65)
tess.left(25)
tess.forward(150)
tess.left(90)
tess.forward(200)
tess.left(90)
tess.forward(150)
tess.left(90)
tess.forward(100)
tess.left(215)
tess.forward(97)
tess.right(100)
tess.forward(56)
tess.clear()
tess.home()
tess.clear()

tess.forward(100)
tess.left(180)
tess.home()
tess.clear()
tess.home()









turtle.exitonclick()
