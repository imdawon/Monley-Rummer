#!/usr/bin/env monkeyrunner
# Operation SnapCrack has begun...

import time #time.sleep(seconds)
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connect MonkeyRunner to device
device = MonkeyRunner.waitForConnection()

# Load pin codes into memory
# I hardcoded the PINs just to make things easier.
# The function to geenrate the PINs
# in numerical order is as follows:
#
#for i in range(0, 10000):
#    print(str(i).zfill(4))
#
f = open("pincodes.txt","r")
pincodes = f.readlines()
f.close()

# 2280x1080 button coordinates
# Access x,y tuples like this:
#
#   x = btn1[0]
#   y = btn1[1]
#
btn1 = (283,934)
btn2 = (538,934)
btn3 = (797,934)
btn4 = (283,1194)
btn5 = (538,1194)
btn6 = (797,1194)
btn7 = (283,1452)
btn8 = (538,1452)
btn9 = (797,1452)
btn0 = (538,1707)
btn_exit_memories = (85,188)
btn_profile = (78,180)
btn_settings = (994,189)
btn_logout = (250,1955)
btn_logout_confirm = (540,1300)
btn_log_in_as = (546,1220)
btn_memories = (343,1887)
btn_my_eyes_only = (900,300)

#monley_inputpin (four-digit pin)
# This function takes a four digit number
# and inputs it into the device.

#monley_pressbutton(btn_name)
# This function takes a button name and
# presses its corresponding location
# on the device.

#monley_swipeup()
# We'll need this function to perform
# a swipe up so we can press the
# logout button.
