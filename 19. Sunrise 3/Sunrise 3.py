from graphics import*;
from Flag import*;
from Person import*;
import random
window = GraphWin("Window",500,500)
j=40
f=0
i=0
e=0
g=0
h=0
n=0
z=0
c=0
counter=0
first = Rectangle(Point(0,0),Point(500,500))
first.draw(window)
first.setFill(color_rgb(0,0,40))
gabe = Rectangle(Point(0,0),Point(500,500))
gabe.draw(window)
for x in range(0,5):
    two = Polygon(Point(54+f,54),Point(50+f,54),
            Point(53.5+f,51),Point(52+f,56),Point(50.5+f,51),
                       Point(54+f,54))
    two.draw(window)
    two.setFill('white')
    two.setOutline('white')
    f=f+100
for x in range(0,4):
    three = Polygon(Point(84+i,104),Point(80+i,104),
            Point(83.5+i,101),Point(82+i,106),Point(80.5+i,101),
                       Point(84+i,104))
    three.draw(window)
    three.setFill('white')
    three.setOutline('white')
    i=i+100
for x in range(0,6):
    four = Polygon(Point(14+e,154),Point(10+e,154),
            Point(13.5+e,151),Point(12+e,156),Point(10.5+e,151),
                       Point(14+e,154))
    four.draw(window)
    four.setFill('white')
    four.setOutline('white')
    e=e+90
for x in range(0,5):
    five = Polygon(Point(54+g,204),Point(50+g,204),
            Point(53.5+g,201),Point(52+g,206),Point(50.5+g,201),
                       Point(54+g,204))
    five.draw(window)
    five.setFill('white')
    five.setOutline('white')
    g=g+100
for x in range(0,6):
    six = Oval(Point(-20+n,250),Point(100+n,350))
    six.draw(window)
    six.setFill('green')
    six.setOutline('green')
    n=n+85
seven = Rectangle(Point(0,275),Point(500,500))
seven.draw(window)
seven.setFill('green')
seven.setOutline('green')
for x in range(0,7):
    y=0
    for x in range(0,20):
        eight = Rectangle(Point(50+y,380+z),Point(70+y,390+z))
        eight.draw(window)
        eight.setFill(color_rgb(80,25,33))
        eight.setOutline(color_rgb(169,169,169))
        y=y+20
    z=z+10
gabetext = Text(Point(225,415),"5...4...3...2...1...")
gabetext.setFill("white")
gabetext.setOutline("white")
gabetext.draw(window)
gabetext.setSize(20)
#Person and Flag
Person.__init__(Person,Point(430,150),window)
Flag.__init__(Flag,Point(0,0),window)
#Sunrise
while(1>0):
    sun1 = Circle(Point(350,210+c),40)
    sun1.setFill("yellow")
    sun1.setOutline("yellow")
    sun1.draw(window)
    window.getMouse()
    c=c-10
    j=j+10
    sun1.undraw()
    first.undraw()
    topleft = sun1.getP1().getY()
    bottomright = sun1.getP2().getY()
    print("Y coordinates: ", topleft, ",", bottomright)
    if(topleft<=0):
        window.close()
    gabe.setFill(color_rgb(0,j,240))










    
