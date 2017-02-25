# EE5900: Intro to Robotics, Project Four - Patrolling

Our implementation of having our robot patrol a region using ROS.

## Development

After cloning this repository, follow these steps to setup the development environment
```
$ cd catkin_ws/src
$ catkin_init_workspace
$ cd ..
$ git submodule init
$ git submodule update
```

Finally, you can build the project and start working on it.

```
$ catkin_make
$ source devel/setup.bash
```

## Implementation

For mapping, use the following command line

```
$ roslaunch patrolling mapping.launch
```

NOTE: rosbag has to be run externally after the launch file completes to log /tf and /front/scan

Once bagged data has been recieved, run gmapping, play the bagged data, and use map_saver to save the obtained map. This is a timed process, so no launch files were created for this

Once mapped data has been obtained, move the pgm and yaml file to the maps folder, and then run

```
$ roslaunch patrolling patrolling.launch
```

to start the random spawner and map patrol.

NOTE: This launch file is a bit unstable, sometimes a node process dies before another one is started, but it works.

