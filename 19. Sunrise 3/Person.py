from Graphics import *;
import random
class Person:
    def __init__(self,point,window):
        self.point = point;
        #point.x = 230
        #point.y = 100
        x = point.getX()
        y = point.getY()
        a=0
        b=0
        f=0
        self.head = Rectangle(Point(x,y),Point(x+40,y+40))
        self.head.draw(window)
        self.head.setFill('red')
        self.body = Rectangle(Point(x-15,y+40),Point(x+55,y+150))
        self.body.draw(window)
        self.body.setFill('blue')
        self.leg1 = Rectangle(Point(x-5,y+150),Point(x+10,y+225))
        self.leg1.draw(window)
        self.leg1.setFill('black')
        self.leg2 = Rectangle(Point(x+30,y+150),Point(x+45,y+225))
        self.leg2.draw(window)
        self.leg2.setFill('black')
        self.sock1 = Rectangle(Point(x-5,y+187.5),Point(x+10,y+225))
        self.sock1.draw(window)
        self.sock1.setFill('white')
        self.sock2 = Rectangle(Point(x+30,y+187.5),Point(x+45,y+225))
        self.sock2.draw(window)
        self.sock2.setFill('white')
        for num in range(0,5):
            self.stripe = Rectangle(Point(x-15,y+50+b),Point(x+55,y+60+b))
            self.stripe.draw(window)
            self.stripe.setFill('green')
            b=b+20
        self.arm1 = Rectangle(Point(x-20,y+50),Point(x-10,y+120))
        self.arm1.draw(window)
        self.arm1.setFill('black')
        self.arm2 = Rectangle(Point(x+50,y+50),Point(x+60,y+120))
        self.arm2.draw(window)
        self.arm2.setFill('black')
        for num in range(0,2):
            g=0
            for num in range(0,4):
                self.sockstripe = Line(Point(x-5+f,y+195+g),Point(x+10+f,y+195+g))
                self.sockstripe.draw(window)
                g=g+5
            f=f+35
    def move(self,dx,dy):
        self.point.x = self.point.x + dx
        self.point.y = self.point.y + dy
        self.head.move(dx,dy)
        self.body.move(dx,dy)
        self.leg1.move(dx,dy)
        self.leg2.move(dx,dy)
        self.sock1.move(dx,dy)
        self.sock2.move(dx,dy)
        self.stripe.move(dx,dy)
        self.arm1.move(dx,dy)
        self.arm2.move(dx,dy)
        self.sockstripe.move(dx,dy)
    def moveTo(self,x,y):
        self.undraw()
        self.__init__(Point(x,y))
