#!/usr/bin/env python
import rospy
import random
import roslaunch

def main():
    x = 5.0;
    y = 5.0;
    #x=random.uniform(-10,10)
    #y=random.uniform(-10,10)
    package = "gazebo_ros"
    executable = "spawn_model"
    argset1 = "-urdf -model jackal -param robot_description -x %f -y %f -z 1.0"%(x,y)
    print argset1
    node = roslaunch.core.Node(package, executable, args=argset1)
    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()
    process = launch.launch(node)



if __name__ == '__main__':
    main()
