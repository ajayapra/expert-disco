#!/usr/bin/env python
import rospy
import random
#import roslaunch
import os

def main():
    # x = 5.0;
    # y = -5.0;
    x=random.uniform(-10,10)
    y=random.uniform(-10,10)
    test = 'rosrun gazebo_ros spawn_model -urdf -model jackal -param robot_description -x "%f" -y "%f" -z 1.0'%(x,y)
    print test
    os.system(test)



if __name__ == '__main__':
    main()
