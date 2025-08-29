################project about to control the drone using keyboard#####################

from djitellopy import Tello
from time import sleep

import keypress_module as kp
kp.init()
me = Tello()
me.connect()
print(me.get_battery())

def getkeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getkey("LEFT"):
        lr = -speed
    elif kp.getkey("RIGHT"):
        lr = speed
    if kp.getkey("UP"):
        fb = speed
    elif  kp.getkey("DOWN"):
        fb = -speed
    if  kp.getkey("w"):
        ud = speed
    elif  kp.getkey("s"):
        ud =speed
    if  kp.getkey("a"):
        yv = speed
    elif  kp.getkey("d"):
        yv=speed
    if  kp.getkey("q"):
        me.land()
    if  kp.getkey("q"):
        me.takeoff()
        

    return[lr, fb, ud, yv]
    

while True:
   values=getkeyboardInput()
   me.send_rc_control(values[0], values[1], values[2], values[3])

