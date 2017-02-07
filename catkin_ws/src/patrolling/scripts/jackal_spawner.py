#!/usr/bin/env python

import rospy
import random
import cv2
import numpy as np
import os

# load the path for the image and read the image file
folder_path = '/home/mano/expert-disco/catkin_ws/src/patrolling/maps/map_dilated.pgm'
img = cv2.imread(folder_path)


def pixel_coordinate():
    pass


def spawn_check():
    pass


def random_point(x, y):
    pass


def main():
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    test = 'rosrun gazebo_ros spawn_model -urdf -model jackal -param robot_description -x "%f" -y "%f" -z 1.0' % (x, y)
    print test
    os.system(test)


if __name__ == '__main__':
    main()
