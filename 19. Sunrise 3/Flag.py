from graphics import *;
from random import *;
#def gotoxy(x,y):
    #print ("%c[%d;%df" % (0x1B, y, x), end='')
class Flag:
    def __init__(flag,point,window):
        flag.point = point
        x2 = point.getX()
        y2 = point.getY()
        flag.one2 = Rectangle(point,Point(x2+17,y2+200))
        flag.one2.setFill('black')
        flag.one2.draw(window)
        flag.two2 = Rectangle(point,Point(x2+300,y2+130))
        flag.two2.setFill('red')
        flag.two2.draw(window)
        d=0
        e=0
        f=0
        g=0
        h=0
        for x in range(0,6):
            flag.three2 = Rectangle(Point(x2,y2+10+d),Point(x2+300,y2+20+d))
            flag.three2.setFill('white')
            flag.three2.setOutline('white')
            flag.three2.draw(window)
            d=d+20
        flag.four2 = Rectangle(point,Point(x2+125,y2+69))
        flag.four2.setFill('blue')
        flag.four2.draw(window)
        flag.one2.setOutline('black')
        flag.two2.setOutline('red')
        flag.four2.setOutline('blue')
        for x in range(0,5):
            f=0
            for x in range(0,6):
                flag.five2 = Polygon(Point(x2+14+f,y2+4+e),Point(x2+10+f,y2+4+e),
                    Point(x2+13.5+f,y2+1+e),Point(x2+12+f,y2+6+e),Point(x2+10.5+f,y2+1+e),
                       Point(x2+14+f,y2+4+e))
                flag.five2.setFill('white')
                flag.five2.setOutline('white')
                flag.five2.draw(window)
                f=f+20
            e=e+15.5
        for x in range(0,4):
            g=0
            for x in range(0,5):
                flag.six2 = Polygon(Point(x2+24+g,y2+11+h),Point(x2+20+g,y2+11+h),
                    Point(x2+23.5+g,y2+8+h),Point(x2+22+g,y2+13+h),Point(x2+20.5+g,y2+8+h),
                       Point(x2+24+g,y2+11+h))
                flag.six2.setFill('white')
                flag.six2.setOutline('white')
                flag.six2.draw(window)
                g=g+20
            h=h+15.5
    def move(flag,dx,dy):
        flag.point.x2 = flag.point.x2+dx
        flag.point.y2 = flag.point.y2+dy
        flag.one2.move(dx,dy)
        flag.two2.move(dx,dy)
        flag.three2.move(dx,dy)
        flag.four2.move(dx,dy)
        flag.five2.move(dx,dy)
        flag.six2.move(dx,dy)
    def moveTo(flag,x2,y2):
        flag.undraw()
        flag.__init__(Point(x2,y2))
    
    
    

