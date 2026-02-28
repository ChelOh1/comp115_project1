import turtle
drawing_screen = turtle.Screen()
drawing_screen.bgcolor("sky blue")

alex = turtle.Turtle()
alex.shape('turtle')
alex.speed(0)
alex.color('navy')

def draw_rectangle(color, x, y, width, height):
    alex.penup()
    alex.goto(x, y)
    alex.begin_fill()
    alex.pendown()
    for _ in range(2):
        alex.forward(width)
        alex.right(90)
        alex.forward(height)
        alex.right(90)
    alex.end_fill()
    alex.penup()

draw_rectangle("navy", -350, -75, 900, 500)

# sun
radius = 10
alex.pensize(5)
alex.penup()
alex.goto(0, -radius)
alex.pendown()
alex.pencolor('orange')
alex.fillcolor('yellow')
alex.color('orange', 'yellow')
alex.begin_fill()
alex.circle(50)
alex.end_fill()
alex.shape("blank")


for i in range(18):
    alex.right(90)
    alex.forward(40)
    alex.back(40)
    alex.left(90)
    alex.circle(50, 20)

    
# cloud
def draw_cloud(x, y):
    cloud = turtle.Turtle()
    cloud.speed(0)
    cloud.shape("circle")
    cloud.color("white")
    cloud.penup()
    cloud.goto(x, y)
    cloud.pendown()
    
    for _ in range(3):
        cloud.begin_fill()
        cloud.circle(30)
        cloud.end_fill()
        cloud.penup()
        cloud.forward(50)
        cloud.pendown()
    cloud.penup()   
    cloud.goto(x - 30, y -30)
    cloud.pendown()
    for _ in range(4):
        cloud.begin_fill()
        cloud.circle(30)
        cloud.end_fill()
        cloud.penup()
        cloud.forward(50)
        cloud.pendown()
        cloud.shape("blank")
        
draw_cloud(-250, 100)
draw_cloud(-150, 200)
draw_cloud(150, 100)
draw_cloud(100, 200)



# wave
alex.color("blue")
alex.pensize(3)

def draw_shape():
    alex.circle(-15, 180)
    alex.circle(15, 180)

positions = [(-310, -100), (-180, -100), (-30, -100), (110, -100), (250, -100), 
    (-230, -150), (-80, -150), (70, -150), (210, -150), (340, -150), 
    (-310, -200), (-180, -200), (-30, -200), (110, -200), (250, -200)
    ]

for x, y in positions:
    alex.penup()
    alex.goto(x, y)
    alex.setheading(90)
    alex.pendown()
    draw_shape()
    
# seagull
alex.color("black")
alex.pensize(3)

def draw_shape():
    alex.circle(-15, 180)
    alex.circle(15, -180)

positions = [(-210, 10), (-270, 30), (150, 10), (200, 30)]

for x, y in positions:
    alex.penup()
    alex.goto(x, y)
    alex.setheading(90)
    alex.pendown()
    draw_shape()

drawing_screen.mainloop()