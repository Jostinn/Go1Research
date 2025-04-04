#! /usr/bin/env python
import rospy
import sys
from unitree_legged_msgs.msg import HighCmd
from unitree_legged_msgs.msg import HighState
import std_msgs.msg
from time import sleep
import pygame

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

    pygame.init()
    size = (300,400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Go1 Keyboard Control")

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

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

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            high_cmd_ros.mode = 2
            high_cmd_ros.gaitType = 1
            high_cmd_ros.velocity = [.5, 0]
        elif keys[pygame.K_s]:
            high_cmd_ros.mode = 2
            high_cmd_ros.gaitType = 1
            high_cmd_ros.velocity = [-.5, 0]
        elif keys[pygame.K_a]:
            high_cmd_ros.mode = 2
            high_cmd_ros.gaitType = 1
            high_cmd_ros.velocity = [0, 0.6]
        elif keys[pygame.K_d]:
            high_cmd_ros.mode = 2
            high_cmd_ros.gaitType = 1
            high_cmd_ros.velocity = [0, -0.6]
        elif keys[pygame.K_q]:
            high_cmd_ros.mode = 2
            high_cmd_ros.gaitType = 1
            high_cmd_ros.yawSpeed = 2
        elif keys[pygame.K_e]:
            high_cmd_ros.mode = 2
            high_cmd_ros.gaitType = 1
            high_cmd_ros.yawSpeed = -2
        elif keys[pygame.K_b]:
            high_cmd_ros.mode = 12
        elif keys[pygame.K_o]:
            #scary but we try it :D
            high_cmd_ros.reserve = 1
            high_cmd_ros.mode = 9
        
    

        pub.publish(high_cmd_ros)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
