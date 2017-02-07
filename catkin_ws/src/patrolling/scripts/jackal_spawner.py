#!/usr/bin/env python

import rospy
import random
import cv2
import numpy as np
import os


# load the path for the image and read the image file
folder_path = '/home/mano/expert-disco/catkin_ws/src/patrolling/maps/map_dilated.pgm'
img = cv2.imread(folder_path)

x_init, y_init, _ = img.shape

loop = True
resolution = 0.02
x_min = -10.88
x_max = x_init * resolution - 20.0
y_min = -8.00
y_max = y_init * resolution - 10.0


def coordinate_to_pixel(x, y):
    global x_min
    global y_min
    ix = round((x - x_min) / 0.02)
    iy = round((y - y_min) / 0.02)
    return ix, iy


def scale_finder(x, y):
    ix, iy = coordinate_to_pixel(x, y)

    return False


def spawn_check(x, y):
    if scale_finder(x, y):
        return True
    else:
        return False


def random_point():
    global loop
    global x_min
    global x_max
    global y_min
    global y_max
    while loop:
        x = random.uniform(x_min+5, x_max+5)
        y = random.uniform(y_min+3, y_max+3)
        loop = spawn_check(x, y)
    return x, y


def main():

    x, y = random_point()
    # test = 'rosrun gazebo_ros spawn_model -urdf -model jackal -param robot_description -x "%f" -y "%f" -z 1.0' % (x, y)
    # amcl = 'roslaunch patrolling amcl_custom.launch initial_x:="%f" initial_y:="%f"' % (x, y)
    # os.system(test)
    # os.system(amcl)

if __name__ == '__main__':
    main()
