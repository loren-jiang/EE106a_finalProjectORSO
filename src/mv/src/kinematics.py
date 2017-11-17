#!/usr/bin/env python
import rospy
from moveit_msgs.srv import GetPositionIK, GetPositionIKRequest, GetPositionIKResponse
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander
import numpy as np
from numpy import linalg

from intera_interface import gripper as robot_gripper
#from intera_interface import gripper as robot_gripper

def move(x, y, z, or_x, or_y, or_z, w, request):
	request.ik_request.pose_stamped.pose.position.x = x
	request.ik_request.pose_stamped.pose.position.y = y
	request.ik_request.pose_stamped.pose.position.z = z
	request.ik_request.pose_stamped.pose.orientation.x = or_x
	request.ik_request.pose_stamped.pose.orientation.y = or_y
	request.ik_request.pose_stamped.pose.orientation.z = or_z
	request.ik_request.pose_stamped.pose.orientation.w = w	

def grab(left_gripper):
#Calibrate the gripper (other commands won't work unless you do this first)
	print('Calibrating...')
	left_gripper.calibrate()
	rospy.sleep(2.0)

	#Close the left gripper
	print('Closing...')
	left_gripper.close()
	rospy.sleep(1.0)

	#Open the left gripper
	print('Opening...')
	left_gripper.open()
	rospy.sleep(1.0)
	print('Done!')

# def takePicture():


def main():
    #Wait for the IK service to become available
    rospy.wait_for_service('compute_ik')
    rospy.init_node('service_query')
    
    #Create the function used to call the service
    compute_ik = rospy.ServiceProxy('compute_ik', GetPositionIK)
    
    # rospy.init_node('gripper_test')
    # #Set up the left gripper
    # left_gripper = robot_gripper.Gripper('left')

    while not rospy.is_shutdown():
        #Construct the request
        request = GetPositionIKRequest()
        request.ik_request.group_name = "left_arm"
        request.ik_request.ik_link_name = "left_gripper"
        request.ik_request.attempts = 20
        request.ik_request.pose_stamped.header.frame_id = "base"

        raw_input('hit enter to move: ')
        move(0.391, -0.326, 0.005, 0., 1., 0., 0., request)
        # raw_input('hit enter to grab: ')
        # grab(left_gripper)
        # request.ik_request.pose_stamped.pose.position.x = 0.391
        # request.ik_request.pose_stamped.pose.position.y = -0.326
        # request.ik_request.pose_stamped.pose.position.z = 0.005
        # request.ik_request.pose_stamped.pose.orientation.x = 0.0
        # request.ik_request.pose_stamped.pose.orientation.y = 1.0
        # request.ik_request.pose_stamped.pose.orientation.z = 0.0
        # request.ik_request.pose_stamped.pose.orientation.w = 0.0
        
        try:
            #Send the request to the service
            response = compute_ik(request)
            
            #Print the response HERE
            print(response)
            group = MoveGroupCommander("left_arm")

            # Setting position and orientation target
            group.set_pose_target(request.ik_request.pose_stamped)

            # TRY THIS
            # Setting just the position without specifying the orientation
            ###group.set_position_target([0.5, 0.5, 0.0])

            # Plan IK and execute
            group.go()
            
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

 
        
        # try:
        #     #Send the request to the service
        #     response = compute_ik(request)
            
        #     #Print the response HERE
        #     print(response)
        #     group = MoveGroupCommander("left_arm")

        #     # Setting position and orientation target
        #     group.set_pose_target(request.ik_request.pose_stamped)

        #     # TRY THIS
        #     # Setting just the position without specifying the orientation
        #     ###group.set_position_target([0.5, 0.5, 0.0])

        #     # Plan IK and execute
        #     group.go()
            
        # except rospy.ServiceException, e:
        #     print "Service call failed: %s"%e

        # raw_input('Move left: ')
        # request.ik_request.pose_stamped.pose.position.x = 0.521
        # request.ik_request.pose_stamped.pose.position.y = 0.165
        # request.ik_request.pose_stamped.pose.position.z = 0.205
        # request.ik_request.pose_stamped.pose.orientation.x = 0.0
        # request.ik_request.pose_stamped.pose.orientation.y = 1.0
        # request.ik_request.pose_stamped.pose.orientation.z = 0.0
        # request.ik_request.pose_stamped.pose.orientation.w = 0.0
        
        # try:
        #     #Send the request to the service
        #     response = compute_ik(request)
            
        #     #Print the response HERE
        #     print(response)
        #     group = MoveGroupCommander("left_arm")

        #     # Setting position and orientation target
        #     group.set_pose_target(request.ik_request.pose_stamped)

        #     # TRY THIS
        #     # Setting just the position without specifying the orientation
        #     ###group.set_position_target([0.5, 0.5, 0.0])

        #     # Plan IK and execute
        #     group.go()
            
        # except rospy.ServiceException, e:
        #     print "Service call failed: %s"%e

        # raw_input('Place down: ')
        # request.ik_request.pose_stamped.pose.position.x = 0.521
        # request.ik_request.pose_stamped.pose.position.y = 0.165
        # request.ik_request.pose_stamped.pose.position.z = 0.005
        # request.ik_request.pose_stamped.pose.orientation.x = 0.0
        # request.ik_request.pose_stamped.pose.orientation.y = 1.0
        # request.ik_request.pose_stamped.pose.orientation.z = 0.0
        # request.ik_request.pose_stamped.pose.orientation.w = 0.0
        
        # try:
        #     #Send the request to the service
        #     response = compute_ik(request)
            
        #     #Print the response HERE
        #     print(response)
        #     group = MoveGroupCommander("left_arm")

        #     # Setting position and orientation target
        #     group.set_pose_target(request.ik_request.pose_stamped)

        #     # TRY THIS
        #     # Setting just the position without specifying the orientation
        #     ###group.set_position_target([0.5, 0.5, 0.0])

        #     # Plan IK and execute
        #     group.go()
            
        # except rospy.ServiceException, e:
        #     print "Service call failed: %s"%e

#Python's syntax for a main() method
if __name__ == '__main__':
    main()

