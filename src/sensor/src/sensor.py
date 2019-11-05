import rospy
from std_msgs.msg import Float32
import logging
import time

from rpisensors.proximity import VL6180X

def talker():
    pub = rospy.Publisher('chatter', Float32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        sensor = VL6180X(1)
        print("publishing = {} mm".format(sensor.read_distance()))
        pub.publish(sensor.read_distance())
        time.sleep(1)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass