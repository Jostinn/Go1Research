#!/usr/bin/python

import sys
import time
import math

sys.path.append('../lib/python/amd64')
import robot_interface as sdk

if __name__ == '__main__':

    HIGHLEVEL = 0xee
    LOWLEVEL = 0xff

    udp = sdk.UDP(HIGHLEVEL, 8080, "192.168.123.161", 8082)

    cmd = sdk.HighCmd()
    state = sdk.HighState()
    udp.InitCmdData(cmd)

    udp.Recv()
    udp.GetRecv(state)

    cmd.mode = 1  # 0:idle, default stand      1:forced stand     2:walk continuously
    cmd.gaitType = 0
    cmd.speedLevel = 0
    cmd.footRaiseHeight = 0
    cmd.bodyHeight = 0
    cmd.euler = [0, 0, 0]
    cmd.velocity = [0, 0]
    cmd.yawSpeed = 0.0
    cmd.reserve = 0


    for x in range(0, 5):
        udp.Recv()
        udp.GetRecv(state)
        if x % 2 == 0:
            cmd.bodyHeight = -.2
        if x % 2 != 0:
            cmd.bodyHeight = 0
        time.sleep(5)
        udp.setSend(cmd)
        udp.Send()
        print(x)

        # cmd.gaitType = 1
        # cmd.mode = 3
        # cmd.speedLevel = 1
        # time.sleep(5)
        # cmd.mode = 0



