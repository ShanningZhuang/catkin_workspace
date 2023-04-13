#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
from control_msgs.msg import GripperCommand

class MoveItFkDemo:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)


        rospy.init_node('moveit_fk_demo', anonymous=True)
 

        left_arm = moveit_commander.MoveGroupCommander('left_arm')

        left_arm.set_goal_joint_tolerance(0.001)
        
        left_arm.set_named_target('home')
        left_arm.go()
        rospy.sleep(2)

        joint_positions = [-0.0867, -1.274, 0.02832, 0.0820, -1.273, -0.003]
        left_arm.set_joint_value_target(joint_positions)
                 
        left_arm.go()
        rospy.sleep(1)
        
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass