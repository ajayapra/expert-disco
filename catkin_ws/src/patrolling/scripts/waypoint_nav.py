#!/usr/bin/env python
import rospy
import actionlib
import random
from move_base_msgs.msg	import MoveBaseAction

def waypoint_nav_node():
    rospy.init_node('waypoint_nav')

    mvbs = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    mvbs.wait_for_server()

    waypoint_index = 0
    rospy.logerr(rospy.get_param('/waypoints_nav/patrolling/waypoints'))

    rospy.loginfo("Waypoint Nav ready.")
    while not rospy.is_shutdown():
        rospy.loginfo(waypoints[waypoint_index])

        mvbs.send_goal(waypoints[waypoint_index])
        mvbs.wait_for_result()
        rospy.loginfo("Nav goal met, setting another one...")

        if len(waypoints) >= waypoint_index:
            waypoint_index = 0
        else:
            waypoint_index = waypoint_index + 1

if __name__ == "__main__":
    waypoint_nav_node()
