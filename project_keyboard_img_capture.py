################project #01# about to click a picture using keyboard#####################

from djitellopy import Tello
from time import sleep
import cv2

import keypress_module as kp
kp.init()
me = Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()

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
    if  kp.getkey("e"):
        me.takeoff()
    if  kp.getkey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return[lr, fb, ud, yv]
    

while True:
   values=getkeyboardInput()
   me.send_rc_control(values[0], values[1], values[2], values[3])
   img= me.get_frame_read().frame
   img=cv2.resize(img,(368,240))
   cv2.imshow("Drone Camera", img)
   cv2.waitKey(1)

