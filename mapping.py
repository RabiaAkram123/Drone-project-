################project #02# about to map the path of drone using keyboard#####################
from djitellopy import Tello
from time import sleep
import numpy as np
import cv2
import math
import keypress_module as kp

#################parameters######################

fspeed = 117 / 10  # forward speed in cm/s (15/s)
aspeed = 360 / 10  # angular speed decrease/s
interval = 0.25
dinterval = fspeed * interval
ainterval = aspeed * interval
x, y = 500, 500
a = 0
yow = 0
###################################################
kp.init()
me = Tello()
me.connect()
print(me.get_battery())
points = [(0,0),(0,0)]


def getkeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    aspeed=50
    global x, y, yow, a
    d = 0

    if kp.getkey("LEFT"):
        lr = -speed
        d = dinterval
        a = -180
    elif kp.getkey("RIGHT"):
        lr = speed
        d = -dinterval
        a = 180
    if kp.getkey("UP"):
        fb = speed
        d = dinterval
        a = 270
    elif kp.getkey("DOWN"):
        fb = -speed
        d = -dinterval
        a = -90
    if kp.getkey("w"):
        ud = speed
    elif kp.getkey("s"):
        ud = speed
    if kp.getkey("a"):
        yv = aspeed
        yow -= ainterval
    elif kp.getkey("d"):
        yv = aspeed
        yow += ainterval
    if kp.getkey("q"):
        me.land()
    if kp.getkey("q"):
        me.takeoff()
    sleep(interval)
    a += yow
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv]

def drawpoints():
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)
    cv2.circle(img, points[-1], 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0]-500)/100},{(points[-1][1]-500)/100}m'
                (points[-1][0]+10, points[-1][1]+30),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1)

while True:
    values = getkeyboardInput()
    me.send_rc_control(values[0], values[1], values[2], values[3])
    img = np.zeros((1000, 1000, 3), np.uint8)
    if (points[-1][0] !=vals[4] or points[-1][1] != vals[5]):
     points.append((vals[4], vals[5]))
    drawpoints()
    cv2.imshow("Output", img)
    cv2.waitKey(1)
