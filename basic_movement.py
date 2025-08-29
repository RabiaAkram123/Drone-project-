################project about to move the drone in basic way#####################

from djitellopy import tello
from time import sleep

me= tello.Tello()
me.connect()    
print(me.get_battery())
me.takeoff()
me.send_rc_control(0, 50, 0, 0)  # Ensure no movement before takeoff
sleep(2)  # Allow time for the command to take effect
me.send_rc_control(30, 0, 0, 0) 
sleep(2) 
me.send_rc_control(0, 0, 0, 0)  # Stop any movement
me.land()
