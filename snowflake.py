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


def snowflake():
    dimx = 300
    dimy = 300
    win = makeWin()
    center = (dimx/2, dimy/2)
    #change the value of xshrink and y shrink to divide the height and width of the blob
    xshrink=1
    yshrink=1
    #change offset to move the circle left or right.
    xoffset=0
    yoffset=0
    numPoints = r.randrange(6, 12)
    for x in range(100): #x affects size outward
        for y in range(12): #y affects number of legs. should be divisible by 6 for an "even" snowflake
            cart = polarToCart(x,y)
            pt = Point(cart[0]/xshrink+center[0]+xoffset,cart[1]/yshrink+center[1]+yoffset)
            pt.draw(win)
            if(x%10==0):
                for z in range(20):
                    #cartnew = polarToCart(x+z,y+z)
                    cartnew = polarToCart(x,y+y*.1)
                    ptnew = Point(cartnew[0]+center[0],cartnew[1]+center[1]+y)
                    ptnew.draw(win)





#this will draw a circle in a single loop, rather than overflowing
def drawCircleNew(n):
    win = makeWin()
    dimx = 300
    dimy = 300
    center = (dimx/2, dimy/2)
    for r in range(n):
        for theta in range(n):
            pt = Point(center[0])


def drawCircle(n):
    win = makeWin()
    for x in range(n):
        for y in range(n):
            pt = Point(x**2, y**2)
            #pt.draw(win)
    dimx = 300
    dimy = 300
    center = (dimx/2, dimy/2)
    for x in range(1,n):
        for y in range(1, n):
            #print(math.sqrt(1-x**2), x)
            # when y = 0, x should be +/-1
            # when x = 0, y should be +/-1
            #pt = Point(center[0]+50*math.sin(y),center[1]+50*math.sin(x))
            pt = Point(center[0]+10*math.cos(x),center[1]+10*math.sin(x))
            pt.draw(win)



def cartToPolar(x,y):
    rho = math.sqrt(x**2 + y**2)
    theta = math.atan(float(y/x))
    return (rho, theta)

def polarToCart(rho,theta):
    x = rho*math.cos(theta)
    y = rho*math.sin(theta)
    return (x,y)

#screen dimension: 1366 x 768
#over 3 = 455 x 256
#int 0 for cartesian coordinates, 1 for polar
#TODO: add moon / other planets 
def randHillTops(cartesian):
    #this will pick like 5 or so points at random and make increasingly
    #large circles going downward
    dimx = 455
    dimy = 256
    center = (dimx/2, dimy/2)
    win = GraphWin("Hilltops", dimx, dimy)
    p = Point(center[0], center[1])
    p.draw(win)
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
        #10 different circle spots 
        for y in range(10):
            cloudx = i+r.randrange(-45, 50)+(y*10)
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

        


def carpets(n):
    win = makeWin()
    for w in range(n):
        locx = r.randrange(0, 280)
        locy = r.randrange(0, 280)
        dimx = r.randrange(10, 30)
        dimy = r.randrange(4, 15)
        dimz = r.randrange(4, 15)
        for x in range(dimx):
            for y in range(dimy):
                for z in range(dimz):
                    #dot = Point(locx+5*x+2*z, locy+5*y)+2*z)
                    dot = Point(locx+5*x+2*z, locy+5*math.sin(5*x)+2*z)
                    dot.draw(win)


def dotCube(n):
    win = makeWin()
    angle = [1,1] #default angle is [2, 2]
    for w in range(n):
        locx = r.randrange(0, 280)
        locy = r.randrange(0, 280)
        dimx = r.randrange(4, 15)
        dimy = r.randrange(4, 15)
        dimz = r.randrange(4, 15)
        for x in range(dimx):
            for y in range(dimy):
                for z in range(dimz):
                    dot = Point(locx+5*x+angle[0]*z, locy+5*y+angle[1]*z)
                    #dot = Point(locx+5*x+2*z, locy+5*math.sin(5*x)+2*z)
                    dot.draw(win)
        for x in range (dimx*5):
            #front box
            pt = Point(locx+x, locy+(dimy*5))
            pt.draw(win)
            pt = Point(locx+x,locy)
            pt.draw(win)
            #back box
            pt = Point(locx+x+(dimz),locy+(dimy*5)+(dimz))
            pt.draw(win)
            #pt = Point(locx, locy+dimy
        for y in range (dimy*5):
            #front box
            pt = Point(locx+(dimx*5),locy+y)
            pt.draw(win)
            pt = Point(locx, locy+y)
            pt.draw(win)
            #back box
        for z in range (dimz*2):
            pt = Point(locx+(dimx*5)+(z/5), locy+(5*dimy)+(z/5))
            pt.draw(win)
            #pt = Point(locx+(dimx*5)+(z/4)-1, locy+(dimy*5)+(z/4))
            #pt.draw(win)

def cubeSpin(n):
    win = makeWin()
    res = [300,300]
    locx = res[0]/2
    locy = res[1]/2
    angle = [2,2] #default angle is [2, 2]
    #each iteration of w is a slightly different angle of the cube
    rect = Rectangle(Point(0,0),Point(300,300))
    rect.setFill("white")
    for w in range(n):
        rect.draw(win)
        dim = 5
        for x in range(dim):
            for y in range(dim):
                for z in range(dim):
                    dot = Point(locx+5*x+angle[0]*z, locy+5*y+angle[1]*z)
                    #dot = Point(locx+5*x+2*z, locy+5*math.sin(5*x)+2*z)
                    dot.draw(win)
        #clear window
        #increase angle. maybe use sin waves for this so they
        angle = [angle[0]-math.sin(w),angle[1]+math.cos(w)]


 


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
        cir2.erase(win)


# 1 1 2 3 5 8 13 21
# if last = 0 then 1
# else return 
def fibonacci(num):
    if num<=1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)


#make with circles of decreasing size? points may be too complicated
# make a line of circles. keep track of last. from last, move in 3 raandom directions. recursive?
def tree():
    dimx = 455
    dimy = 256
    center = (dimx/2, dimy/2)
    win = GraphWin("tree", dimx, dimy)
    for x in range(20):
        print()
        for y in range(20):
            print()




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
            randHillTops(0)
        elif(cont == 't'):
            x = float(input("enter x: "))
            y = float(input("enter y: "))
            cartToPolarTest(x, y)
        elif(cont == 'o'):
            snowflake()
        elif(cont == 'd'):
            cubes = int(input("enter number of cubes: "))
            dotCube(cubes)
        elif(cont == 'dd'):
            carpets(10)
        elif(cont == 'cs'):
            cubeSpin(10)

        cont = input("MENU\n cs - cube spin\n dd - carpets\n d - dotcube\n o - snowflake\n t - cartToPolarTest\n h - random hill tops\n a - circle draw\n n - fib\n c - random circles\n q - quit\n p - point line\n r - random shape\n")
    print("Have a cool chill day!")




