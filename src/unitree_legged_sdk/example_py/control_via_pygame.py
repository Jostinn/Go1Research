#!/usr/bin/python

import sys
import time
import math
import pygame

sys.path.append('../lib/python/amd64')
import robot_interface as sdk

if __name__ == '__main__':

    HIGHLEVEL = 0xee
    LOWLEVEL = 0xff

    udp = sdk.UDP(HIGHLEVEL, 8080, "192.168.123.161", 8082)

    cmd = sdk.HighCmd()
    state = sdk.HighState()
    udp.InitCmdData(cmd)

    pygame.init()

    size = (300, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Go1 Keyboard Control")

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        udp.Recv()
        udp.GetRecv(state)

        # print(motiontime)
        # print(state.imu.rpy[0])
        # print(motiontime, state.motorState[0].q, state.motorState[1].q, state.motorState[2].q)
        # print(state.imu.rpy[0])

        cmd.mode = 0  # 0:idle, default stand      1:forced stand     2:walk continuously
        cmd.gaitType = 0
        cmd.speedLevel = 0
        cmd.footRaiseHeight = -0.04  # Keefe: (-) is lower (+) is higher | change in small increments (0.01)
        cmd.bodyHeight = 0
        cmd.euler = [0, 0, 0]
        cmd.velocity = [0, 0]  # Keefe: x is forward / back and y is side | DO NOT CHANGE HERE
        cmd.yawSpeed = 0.0  # Keefe: way it rotates (+) CCW (-) CW | DO NOT CHANGE HERE
        cmd.reserve = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            cmd.mode = 2
            cmd.gaitType = 1
            cmd.velocity = [.3, 0]  # Keefe: usually 0.6 - slowed down to see step height
        elif keys[pygame.K_s]:
            cmd.mode = 2
            cmd.gaitType = 1
            cmd.velocity = [-.3, 0] # Keefe: usually -0.6 - slowed down to see step height
        elif keys[pygame.K_a]:
            cmd.mode = 2
            cmd.gaitType = 1
            cmd.velocity = [0, 0.6]
        elif keys[pygame.K_d]:
            cmd.mode = 2
            cmd.gaitType = 1
            cmd.velocity = [0, -0.6]
        elif keys[pygame.K_q]:
            cmd.mode = 2
            cmd.gaitType = 1
            cmd.yawSpeed = 1
        elif keys[pygame.K_e]:
            cmd.mode = 2
            cmd.gaitType = 1
            cmd.yawSpeed = -1
        elif keys[pygame.K_b]:
            cmd.mode = 12
        elif keys[pygame.K_o]:
            cmd.mode = 9
        elif keys[pygame.K_SPACE]:
            cmd.mode = 1

        udp.SetSend(cmd)
        udp.Send()
