#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import random


ev3 = EV3Brick()

leftright = Motor(Port.A)
robotarm = Motor(Port.C)
updown = Motor(Port.B)
surrender = Motor(Port.D)

switch = ColorSensor(Port.S4)
handdetect = UltrasonicSensor(Port.S3)

fifty = [0,1]
rgb = []
impossible = []
leftmoved = 0
push = 0

for _ in range(14) :
    impossible.append(0)

impossible.append(1)

while True :
    if handdetect.distance() <= 150 :
        if random.choice(fifty) == 0 :
            if leftmoved == 0 :
                leftright.run_angle(1560, 600, then=Stop.HOLD, wait=True)
                leftmoved = 1
            else :
                leftright.run_angle(1560, -600, then=Stop.HOLD, wait=True)
                leftmoved = 0
        elif random.choice(fifty) == 1 :
            updown.run_angle(2000, -80, then=Stop.HOLD, wait=True)
            wait(1500)
            updown.run_angle(2000, 80, then=Stop.HOLD, wait=True)
    elif handdetect.distance() > 150 :
        rgb = list(switch.rgb())
        if rgb[0] >= 5:
            if random.choice(impossible) == 0 :
                if random.choice(fifty) == 0 :
                    push += 1
                    robotarm.run_angle(2000, -95, then=Stop.HOLD, wait=True)
                    robotarm.run_angle(2000, 95, then=Stop.HOLD, wait=True)
                elif random.choice(fifty) == 1 :
                    push += 1
                    robotarm.run_angle(2000, -45, then=Stop.HOLD, wait=True)
                    wait(500)
                    robotarm.run_angle(2000, -50, then=Stop.HOLD, wait=True)
                    robotarm.run_angle(2000, 95, then=Stop.HOLD, wait=True)
                
                if push == 37 :
                    ev3.speaker.beep()
                    updown.run_angle(2000, -80, then=Stop.HOLD, wait=True)
                    wait(5000)
                    updown.run_angle(2000, 80, then=Stop.HOLD, wait=True)
                    push = 0
            elif random.choice(impossible) == 1 :
                wait(3000)
                surrender.run_angle(25, 90, then=Stop.HOLD, wait=False)
                ev3.speaker.play_notes(['C5/4.','G4/4.','E4/4','A4/4','B4/4','A4/4','Ab4/4','Bb4/4','Ab4/4','G4/4_','G4/4_','G4/4_','G4/4_'], tempo=200)
                surrender.run_angle(1560, -90, then=Stop.HOLD, wait=True)
                wait(5000)
                robotarm.run_angle(2000, -95, then=Stop.HOLD, wait=True)
                robotarm.run_angle(2000, 95, then=Stop.HOLD, wait=True)
                push = 0