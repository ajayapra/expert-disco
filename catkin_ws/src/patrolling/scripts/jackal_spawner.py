#!/usr/bin/env python

import rospy
import random
import cv2
import numpy as np
import os


# load the path for the image and read the image file
folder_path = '/home/robotics4/expert-disco/catkin_ws/src/patrolling/maps/map_obstacle_dilated.pgm'
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
    check_seg = img[ix-10:ix+10, iy-10:iy+10, 0]

    check_seg_np = np.array(check_seg)
    check_seg_np = np.concatenate(check_seg_np, axis=0)

    idx = np.where(check_seg_np < 240)
    return idx


def spawn_check(x, y):
    if np.sum(scale_finder(x, y)) > 0:
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
        x = random.uniform(-8, 8)
        y = random.uniform(-6, 6)
        loop = spawn_check(x, y)
    return x, y


def main():

    x, y = random_point()
    # print(x)
    # print(y)
    test = 'rosrun gazebo_ros spawn_model -urdf -model jackal -param robot_description -x "%f" -y "%f" -z 1.0' % (x, y)
    amcl = 'roslaunch patrolling amcl_custom.launch initial_x:="%f" initial_y:="%f"' % (x, y)
    os.system(test)
    os.system(amcl)

if __name__ == '__main__':
    main()
