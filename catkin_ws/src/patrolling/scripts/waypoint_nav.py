#!/usr/bin/env python
import rospy
import actionlib
from geometry_msgs.msg import Pose, PoseStamped
from move_base_msgs.msg	import MoveBaseGoal, MoveBaseAction
from visualization_msgs.msg import MarkerArray, Marker

class WaypointNav(object):
    def __init__(self):
        self.waypoints = []
        self.waypoint_index = 0

        rospy.init_node('waypoint_nav')

        for wp in rospy.get_param('/waypoints_nav/patrolling/waypoints'):
            temp = MoveBaseGoal()

            temp.target_pose.header.frame_id = 'map'
            temp.target_pose.pose.position.x = wp['x']
            temp.target_pose.pose.position.y = wp['y']
            temp.target_pose.pose.position.z = wp['z']

            temp.target_pose.pose.orientation.w = 1

            self.waypoints.append(temp)

        self.mvbs = actionlib.SimpleActionClient('move_base', MoveBaseAction)

        self.sub = rospy.Subscriber("move_base_simple/goal", PoseStamped,
                                    self._update_waypoints)

        self.viz_pub = rospy.Publisher("patrolling/viz_waypoints_array",
                                       MarkerArray, queue_size=10)
        self._publish_markers()

        rospy.loginfo("Waypoint Nav ready.")

    def _update_waypoints(self, data):
        latest = MoveBaseGoal(target_pose = data)

        if rospy.get_param('/waypoints_nav/patrolling/update_patrol'):
            self.waypoints.insert(self.waypoint_index, latest)

            if rospy.get_param('/waypoints_nav/patrolling/save_latest'):
                ros.set_param_raw('/waypoints_nav/patrolling/waypoints',
                                  self.waypoints)

    def _publish_markers(self):
        markers = []
        id = 0
        for wp in self.waypoints:
            temp = Marker()

            # temp.header = wp.target_pose.header
            temp.id = id
            temp.ns = "patrolling"
            temp.action = Marker.ADD

            temp.type = Marker.CUBE
            temp.pose = wp.target_pose.pose
            temp.scale.x = 1
            temp.scale.y = 1
            temp.scale.z = 1
            temp.color.a = 1
            temp.color.r = 1
            temp.color.g = 1
            temp.color.b = 1

            markers.append(temp)
            id = id + 1

        self.viz_pub.publish(markers=markers)
        rospy.loginfo("Markers Published")

    def start_nav(self):
        self.mvbs.wait_for_server()

        while not rospy.is_shutdown():
            rospy.loginfo(self.waypoints[self.waypoint_index])

            self._publish_markers()

            self.mvbs.send_goal(self.waypoints[self.waypoint_index])
            self.mvbs.wait_for_result()
            rospy.loginfo("Nav goal met, setting another one...")

            if self.waypoint_index >= len(self.waypoints):
                self.waypoint_index = 0
            else:
                self.waypoint_index = self.waypoint_index + 1

if __name__ == "__main__":
    WaypointNav().start_nav()
