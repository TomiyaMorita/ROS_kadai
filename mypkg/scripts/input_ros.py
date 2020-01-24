#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def mode():
    pub = rospy.Publisher('mode_gpio', String, queue_size=10)
    rospy.init_node('mode', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
         str = raw_input()       
         rospy.loginfo(str)
         pub.publish(str)
         rate.sleep()

if __name__ == '__main__':
    try:
        mode()
    except rospy.ROSInterruptException: pass



