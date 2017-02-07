#!/usr/bin/env python

import rospy
import random
import cv2
import numpy as np
import os


# load the path for the image and read the image file
folder_path = '/home/mano/expert-disco/catkin_ws/src/patrolling/maps/map_dilated.pgm'
img = cv2.imread(folder_path)

x_init, y_init, _ = img.shape()

loop = True
resolution = 0.02
xmin = -20.88
xmax = x_init*resolution + xmin
ymin = -10.00
ymax = y_init*resolution + ymin

def scale_finder(ix, iy):
    # ix, iy = coordinate_to_pixel(x, y)
    

def coordinate_to_pixel(x, y):
    global xmin, ymin
    ix = round((x-xmin)/0.02)
    iy = round((y-ymin)/0.02)
    return ix, iy


def spawn_check(x, y):
    if scale_finder(x, y):
        return True
    else:
        return False

def random_point():
    global loop
    global xmin, xmax, ymin, ymax
    while loop:
        x = random.uniform(xmin, xmax)
        y = random.uniform(ymin, ymax)
        loop = spawn_check(x, y)
    return x, y


def main():
    x, y = random_point()

    test = 'rosrun gazebo_ros spawn_model -urdf -model jackal -param robot_description -x "%f" -y "%f" -z 1.0' % (x, y)
    print test
    os.system(test)


if __name__ == '__main__':
    main()
