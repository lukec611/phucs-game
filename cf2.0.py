from turtle import *
import circle_collision
import time
sc = Screen()
count = 0
z = count

shoty = Turtle()

display = Turtle()
display.penup()
display.setpos(-330, 330)
display.write('no message')

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 50
        self.init_turtle()
    def init_turtle(self):
        self.turtle = Turtle()
        self.turtle.resizemode('user')
        self.turtle.penup()
        self.turtle.shape('circle')
        self.turtle.shapesize(self.radius * 0.1, self.radius * 0.1, 1)
        self.turtle.color('red')
        self.turtle.setpos(self.x, self.y)
    def is_touching_player(self):
        playerPos = shoty.pos()
        return circle_collision.circles_collide(
            self.x,
            self.y,
            self.radius,
            playerPos[0],
            playerPos[1],
            8
        )
e1 = Enemy(50.0, 100.0)

def on_move():
    msg = 'nothing to report'
    if e1.is_touching_player():
        msg = 'Player touches enemy'
    display.clear()
    display.write(msg, font=('Arial', 18, 'normal'))
    
    

sc.title('you')
pen = Turtle()
pen.ht()
pen.penup()
pen.backward(50)

shoty.ht()
shoty.penup()
shoty.setpos (0,-300)
#shoty.shape('triangle')
shoty.shapesize(3)
shoty.left(90)
shoty.speed(2)
def showcontent():
    pen.write('welcome', font=('Arial', 50, 'normal'))
    time.sleep(0.3) # show welcome for 3 seconds
    for i in range (10,0,-1):
        pen.clear()
        pen.write(str(i), font=('Arial', 40, 'normal'))
        time.sleep(0.1) # wait 1 second before showing the next number in the countdown
        pen.clear()
    shoty.st()
    display.clear()
    display.write('nothing to report', font=('Arial', 18, 'normal'))
SB = Turtle()
SB.penup()
SB.shape('circle')
SB.color('red')
SB.shapesize(20)
def start(x,y):
    SB.ht()
    SB.clear()
    showcontent()
    
def mr():
    shoty.right(10)
    on_move()

def ml():
    shoty.left(10)
    on_move()

def forward():
    shoty.forward(15)
    on_move()
def backward():
    shoty.backward(15)
    on_move()
    
SB.onclick(start)
bulletList = []
def shoot(x,y):
        x = shoty.xcor()
        y = shoty.ycor()
        z = Turtle()
        z.penup()
        z.setpos(x,y)
        z.left(90)
        z.speed(0)
        z.shape('circle')
        bulletList.append(z)        
def ontimer():
    for index in range(len(bulletList)):
        bl = bulletList[index]
        bl.forward(10)
        
    for index in range(len(bulletList)):
        if bl.ycor()>500:
            del bulletList[index]
    sc.ontimer(ontimer, 250)

ontimer()
sc.onclick(shoot)
shoty.onclick(shoot)
sc.onkey(forward, "w")
sc.onkey(backward, "s")
sc.onkey(ml, "a")
sc.onkey(mr, "d")
listen()
EB = Turtle()
EB.penup()
EB.shape('triangle')
EB.color('yellow')
EB.shapesize(4)
EB.setpos(627,-300)
def exist(x,y):
    sc.bye()
EB.onclick(exist)

mainloop()
# sc.mainloop()



