#!/usr/bin/env monkeyrunner
# Operation SnapCrack has begun...

import time #time.sleep(seconds)
import argparse

parser = argparse.ArgumentParser(description='Bruteforce Snapchat\'s my eyes only pin code')
parser.add_argument('--simulate',
                    action='store_true',
                    help='Do not interact with the device')
parser.add_argument('-d',
                    '--device',
                    type=str,
                    metavar='',
                    required=True,
                    help='Either pixel or s10')
args = parser.parse_args()

if not args.simulate:
    from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Button coordinates
# Access x,y tuples like this:
#
#   x = btn1[0]
#   y = btn1[1]
#
if args.device == "galaxy":
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

elif args.device == "pixel":
    btn1 = (383,1159)
    btn2 = (750,1159)
    btn3 = (1030,1159)
    btn4 = (383,1500)
    btn5 = (750,1500)
    btn6 = (1030,1500)
    btn7 = (383,1836)
    btn8 = (750,1836)
    btn9 = (1030,1836)
    btn0 = (750,2117)
    btn_exit_memories = (118,234)
    btn_profile = (118,234)
    btn_settings = (1288,203)
    btn_logout = (689,2476)
    btn_logout_confirm = (507,1620)
    btn_log_in_as = (507,1550)
    btn_memories = (710,2541)
    btn_my_eyes_only = (1136,356)

# monley_inputpin() needs this 
# in order to convert numbers as
# a string into buttons.
button = {
    1: btn1,
    2: btn2,
    3: btn3,
    4: btn4,
    5: btn5,
    6: btn6,
    7: btn7,
    8: btn8,
    9: btn9,
    0: btn0
}

def monley_inputpin(pin):
    for number in pin:
        print(number)
        device.touch(button[int(number)][0], button[int(number)][1], MonkeyDevice.DOWN_AND_UP)
        time.sleep(.1)

# This function takes a button name and
# presses its corresponding location
# on the device.
def monley_pressbutton(btn_name):
    device.touch(btn_name[0], btn_name[1], MonkeyDevice.DOWN_AND_UP)

# This function performs a swipe-up
def monley_swipeup():
    device.drag((700,1500), (700,900), .05, 3)

# This function performs a
# specific number of swipe-ups
def monley_swipeup(swipes):
    for x in range(1, swipes+1):
        device.drag((700,1500), (700,900), .05, 3)
        time.sleep(.3)



### PROGRAM STARTS HERE

# Connect MonkeyRunner to device
if not args.simulate:
    print("Waiting for device connection...")
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
pincodes = [endl.strip() for endl in pincodes]
f.close()

for x in range(0,5):
    print ("PIN: " + pincodes[x])
    
    if not args.simulate:
        monley_inputpin(pincodes[x])

    time.sleep(1)
