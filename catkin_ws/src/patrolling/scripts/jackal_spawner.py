#!/usr/bin/env python
import rospy
import random
#import roslaunch
import os

def main():
    x=random.uniform(-10,10)
    y=random.uniform(-10,10)
    test = 'rosrun gazebo_ros spawn_model -urdf -model jackal -param robot_description -x "%f" -y "%f" -z 1.0'%(x,y)
    amcl = 'roslaunch patrolling amcl_custom.launch initial_x:="%f" initial_y:="%f"'%(x,y)
    os.system(test)
    os.system(amcl)
if __name__ == '__main__':
    main()
