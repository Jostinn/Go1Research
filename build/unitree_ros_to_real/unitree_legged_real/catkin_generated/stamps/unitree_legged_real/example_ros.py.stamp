#! /usr/bin/env python
import rospy
import sys
from unitree_legged_msgs.msg import HighCmd
from unitree_legged_msgs.msg import HighState
import std_msgs.msg
from time import sleep

#sys.path.append('../lib/python/amd64')
#import robot_interface as sdk

def main():
    rospy.init_node('example_walk_without_lcm')
    print("WARNING: Control level is set to HIGH-level.")
    print("Make sure the robot is standing on the ground.")
    input("Press Enter to continue...")

    pub = rospy.Publisher('high_cmd', HighCmd, queue_size=1000)
    rospy.sleep(1)

    motiontime = 0

    rate = rospy.Rate(500)

    while not rospy.is_shutdown():
        motiontime += 2

        high_cmd_ros = HighCmd()
        high_cmd_ros.head = [0xFE, 0xEF]
        high_cmd_ros.levelFlag = 0xee
        high_cmd_ros.mode = 0
        high_cmd_ros.gaitType = 0
        high_cmd_ros.speedLevel = 0
        high_cmd_ros.footRaiseHeight = 0
        high_cmd_ros.bodyHeight = 0
        high_cmd_ros.euler = [0, 0, 0]
        high_cmd_ros.velocity = [0.0, 0.0]
        high_cmd_ros.yawSpeed = 0.0
        high_cmd_ros.reserve = 0

        if (motiontime > 0 and motiontime < 1000):
            high_cmd_ros.mode = 2
            high_cmd_ros.gaitType = 1
            high_cmd_ros.velocity = [-.5,0]
    

        pub.publish(high_cmd_ros)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
