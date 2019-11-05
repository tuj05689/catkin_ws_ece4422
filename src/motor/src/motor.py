#!/usr/bin/env python

import rospy
from gpiozero import Servo
from time import sleep

from std_msgs.msg import Float32


def callback(data):
    print("Sub distance: {} mm".format(data.data))
    x = data.data
    if x < 90:
        y = -x/190
    elif x>90 and x<190:
        y = x/190
    else:
        y = x/255
    servo.value = y
    sleep(.1)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    servoPIN = 21  # this must be the GPIO# not the physical pin #. e.g. to use pin$
    moveDelay = 1
    myCorrection = 0.2  # used to correct the motion of the servo. It is servo spec$
    maxPW = (2.0 + myCorrection) / 1000
    minPW = (1.0 - myCorrection - .1) / 1000
    servo = Servo(servoPIN, min_pulse_width=minPW, max_pulse_width=maxPW)
    servo.value = -1
    sleep(moveDelay)
    servo.value = 1
    sleep(moveDelay)
    listener()
