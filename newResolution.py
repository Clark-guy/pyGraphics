import time as t
import random as r
import math
import numpy
from graphics import *




def makeWinRuler():
    win = GraphWin('Ruler', 300, 300)
    for x in range(30):
        pt = Point(x*10, 0)
        pt1 = Point(0, x*10)
        pt2 = Point(x*10, x*10)
        cir = Circle(Point(150, 150), 150)
        cir.draw(win)
        pt.draw(win)
        pt1.draw(win)
        pt2.draw(win)

def makeWin():
    return GraphWin('Window', 300, 300)

#given two points, make a bunch of points between them
def pointLine(sx, sy, ex, ey):
    win = makeWin()
    #given point at 2,3 and 5,8: first x should be (sx, sy) last should be (ex, ey)
    #at each point x there will be a new dot at 
    #y = mx + b
    slope = ((ey-sy)/(ex-sx))
    b = sy-slope*sx
    while(sx!=ex):
        pt = Point(sx,slope*sx+b)
        pt.draw(win)
        if(sx<ex):
            sx+=1
        else:
            sx-=1
        t.sleep(.05)

#create random point, draw line from last point, repeat
def randShape():
    win = makeWin()
    #initialize start x and y at center
    sx = 150
    sy = 50
    #number of edges in shape
    numEdges = r.randrange(4, 10)
    for y in range(numEdges):
        #pick random point on window for end x and y
        if(y != numEdges-1):
            ex = r.randrange(1, 300)
            ey = r.randrange(1, 300)
        else:
            ex = 150
            ey = 50
        #calculate slope and y intercept
        if(ex-sx==0):
            slope = .01
        else:
            slope = ((ey-sy)/(ex-sx))
        b=sy-slope*sx
        #draw the line in this loop. init x
        while(sx!=ex):
            pt = Point(sx, sx*slope+b)
            pt.draw(win)
            if(sx<ex):
                sx+=1
            else:
                sx-=1
            #t.sleep(.01)
        sx = ex
        sy = ey


def circleRandom(numCircles):
    win = makeWin()
    for x in range(numCircles):
        #cir = graph starts at 0, 0 in upper left. coords are x, y
        cir = Circle(Point(r.randrange(0, 200), r.randrange(0, 200)), r.randrange(1, 50))
        cir.draw(win)
        for x in range(1,5):
            cir.move(r.randrange(25)/x, r.randrange(25)/x)
            #t.sleep(.05)

def drawCircle(n):
    win = makeWin()
    for x in range(n):
        for y in range(n):
            pt = Point(x**2, y**2)
            pt.draw(win)


#screen dimension: 1366 x 768
#over 3 = 455 x 256
#TODO: add moon / other planets 
def randHillTops():
    #this will pick like 5 or so points at random and make increasingly
    #large circles going downward
    dimx = 455
    dimy = 256

    win = GraphWin("Hilltops", dimx, dimy)
    #create hills, mts
    for x in range(r.randrange(int(dimx/100), int(dimx/40))):
        i = r.randrange(0,dimx)
        j = dimy-r.randrange(30, 170)
        jlopez = dimy-r.randrange(20,50)
        pt = Point(i,j)
        logvals = [100,1000, 10000, 100000]
        logval = r.randrange(0,3)
        for y in range(20):
            if(logval == (2 or 3)):
                cir = Circle(Point(i,(jlopez+y*10)),y*math.log(logvals[logval]))
            else:
                cir = Circle(Point(i,(j+y*10)),y*math.log(logvals[logval]))
            cir.draw(win)
            t.sleep(.03)
    #create clouds - make line of clouds along top
    #number of clouds depends on length of window
    for x in range(int(dimx/100)):
        i = r.randrange(0,dimx)
        j = r.randrange(0,int(dimy/3))
        
        for y in range(10):
            cloudx = i+r.randrange(-49, 50)
            cloudy = j+r.randrange(-9,10)
            #cir = Circle(Point(cloudx,cloudy), j/5)
            for z in range(5):
                cir = Circle(Point(cloudx+z,cloudy+z), j/5+z)
                cir.draw(win)
            t.sleep(.1)
    #create background mts
    for x in range(r.randrange(1,4)):
        last=((int(dimy*2/3)))+20*x
        for y in range(0,dimx):
            cur = last+r.randrange(-3,4)
            pt = Point(y, cur)
            pt.draw(win)
            last = cur

        


def newShit(n):
    i = 300
    j = 300
    k = 300
    win = makeWin()
    #arr = numpy.zeros((i,j,k))
    for x in range(i):
        #arr = arr[x, y, z]
        cir = Circle(Point(x, 150+math.sin(x/5)*30), x+5)
        #cir2 = Circle(Point(math.tan(x**2-i)+150, x**2), 20.5-x**2)
        cir2 = Circle(Point(150+math.cos(x/10)*20,x), 40*math.sin(x/168))
        cir.draw(win)
        cir2.draw(win)
        t.sleep(.01)


# 1 1 2 3 5 8 13 21
# if last = 0 then 1
# else return 
def fibonacci(num):
    if num<=1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)



if __name__ == '__main__':
    cont = 's'
    while(cont != 'q'):
        if(cont == 'c'):
            num = int(input("how many circles?\n"))
            circleRandom(num)
        elif(cont == 'p'):
            x = int(input("enter x1, y1, x2, and y2\n"))
            y = int(input(""))
            x2 = int(input(""))
            y2 = int(input(""))
            pointLine(x,y,x2,y2)
        elif(cont == 'r'):
            randShape()
        elif(cont == 'n'):
            x = int(input("enter a number: "))
            newShit(x)
        elif(cont == 'a'):
            x = int(input("number: "))
            drawCircle(x)
        elif(cont == 'h'):
            randHillTops()
        cont = input("MENU\n h - random hill tops\n a - circle draw\n n - fib\n c - random circles\n q - quit\n p - point line\n r - random shape\n")
    print("Have a cool chill day!")




