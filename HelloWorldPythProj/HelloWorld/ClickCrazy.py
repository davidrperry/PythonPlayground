
#Imports
import imp
import time
from helpers.GraphicsHelper import GraphicsHelper
from builtins import print
from random import randint
from subprocess import call

#Fields
mod = GraphicsHelper.GetGraphicsModule()

windSize = 700
objSize = 50
objs = list()
speed = 2
score = 0
minSleep = 0.00
win = mod.GraphWin("Click Crazy", windSize, windSize)
text = mod.Text(mod.Point((windSize/2),15),'Score: ' + str(score))


def startGame():
    rect = mod.Rectangle(mod.Point(0,0), mod.Point(objSize,objSize))
    rect.draw(win)
    text.draw(win)
    objs.append(rect)

def moveItems():
    for x in objs:
        moveObjecRand(x)

def gamePlay():
    if (validSpeed()):
        moveItems()
        time.sleep(speed)
            

def InsideRectangle(point, obj):
	if (point == None):
		return False
	y = point.getY()
	x = point.getX()
	uY = obj.getP1().getY()
	leX = obj.getP1().getX()
	lY = obj.getP2().getY()
	rX = obj.getP2().getX()

	if ((y >= uY and y <= lY) and (x <= rX and x >= leX)):
		return True
	return False

def CloneObject(object, y, x ):
    clone = object.clone()
    clone.draw(win)
    return clone

def addItem():
    objs.append(CloneObject(objs[0],0,0))

def RandNumber():
    return randint(objSize,windSize)

def UpdateScore():
    global score
    global speed
    score += 1
    speed -= 0.1
    text.setText('Score: ' + str(score))

def moveObjecRand(obj):
    rightX = RandNumber()
    lowerY = RandNumber()

    lowRPoint = obj.getP2()
    x = lowRPoint.getX()
    y = lowRPoint.getY()
    obj.move((rightX - x), (lowerY - y))

def ClickInAny(point):
    isClick = False
    for x in objs:
        if (InsideRectangle(point, x)):
            return True
    return False

def Winner():
    text = mod.Text(mod.Point((windSize/2),(windSize/2)), 'Congragulations you beat the game')
    text.draw(win)
    time.sleep(10)

def UndrawAll():
    for x in objs:
        x.undraw()
    text.undraw()

def validSpeed():
    return speed >= minSleep 

startGame()

while validSpeed():
    try:
        while ClickInAny(win.checkMouse()) == False and validSpeed():
            gamePlay()
        UpdateScore()
        addItem()
        if(validSpeed() == False):
            break
    except KeyboardInterrupt:
        break

UndrawAll()
Winner()
win.close()
