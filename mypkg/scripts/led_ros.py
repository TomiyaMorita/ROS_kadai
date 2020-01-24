#!/usr/bin/env python

import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import String
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
    
def callback(data):  
    if (data.data == 'a'):
        GPIO.output(11, True)
    elif(data.data == 'b'):
        GPIO.output(11, False)
    if (data.data == 'c'):
        GPIO.output(9, True)
    elif(data.data == 'd'):
        GPIO.output(9, False)
    if (data.data == 'e'):
        GPIO.output(10, True)
    elif(data.data == 'f'):
        GPIO.output(10, False)

def listener():
   
       # in ROS, nodes are unique named. If two nodes with the same
       # node are launched, the previous one is kicked off. The
       # anonymous=True flag means that rospy will choose a unique
       # name for our 'listener' node so that multiple listeners can
       # run simultaenously.
       rospy.init_node('listener', anonymous=True)
  
       rospy.Subscriber("mode_gpio", String, callback)
  
       # spin() simply keeps python from exiting until this node is stopped
       rospy.spin()
  
if __name__ == '__main__':
    listener()
    GPIO.cleanup()

