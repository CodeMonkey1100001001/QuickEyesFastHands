# QuickEyesFastHands.py
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import random

portList = [
    DigitalInOut(board.D6),
    DigitalInOut(board.D9),
    DigitalInOut(board.D10),
    DigitalInOut(board.D11),
    DigitalInOut(board.A0),
    DigitalInOut(board.A1),
    DigitalInOut(board.A2),
    DigitalInOut(board.A3)
    ]

portDrop=[0,0,0,0, 0,0,0,0]
portDropOrder=[0,1,2,3, 4,5,6,7]
print("portDropOrder["+str(portDropOrder))
portDropOrder= sorted(portDropOrder, key=lambda x: random.random())
print("portDropOrder="+str(portDropOrder))

for aPort in portList:
    aPort.direction = Direction.OUTPUT
    aPort.value=True
 
switch = DigitalInOut(board.D5)  # For Feather M0 Express, Feather M4 Express
switch.direction = Direction.INPUT
switch.pull = Pull.UP

walkPosition=0

while True:
    if switch.value:
        pass
        #print("nothing")
    else:
        print("drop")
        while walkPosition<8:
            time.sleep(2.00+(random.randrange(25)/10))
            portList[portDropOrder[walkPosition]].value=False
            walkPosition=walkPosition+1
            print("walkPosition="+str(walkPosition))

        time.sleep(2.0)

        for aPort in portList:
            aPort.value=True
        walkPosition=0
        portDropOrder= sorted(portDropOrder, key=lambda x: random.random())
        print("reset it")

    time.sleep(0.1)
  
