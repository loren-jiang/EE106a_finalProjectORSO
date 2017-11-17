#!/usr/bin/env python
import rospy
from moveit_msgs.srv import GetPositionIK, GetPositionIKRequest, GetPositionIKResponse
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander
import numpy as np
from numpy import linalg

def move(x, y, z, or_x, or_y, or_z, w, request):
	request.ik_request.pose_stamped.pose.position.x = x
	request.ik_request.pose_stamped.pose.position.y = y
	request.ik_request.pose_stamped.pose.position.z = z
	request.ik_request.pose_stamped.pose.orientation.x = or_x
	request.ik_request.pose_stamped.pose.orientation.y = or_y
	request.ik_request.pose_stamped.pose.orientation.z = or_z
	request.ik_request.pose_stamped.pose.orientation.w = w	

def main():
    #Wait for the IK service to become available
    rospy.wait_for_service('compute_ik')
    rospy.init_node('service_query')
    
    #Create the function used to call the service
    compute_ik = rospy.ServiceProxy('compute_ik', GetPositionIK)
    
    while not rospy.is_shutdown():
        #Construct the request
        request = GetPositionIKRequest()
        request.ik_request.group_name = "right_arm"
        request.ik_request.ik_link_name = "right_gripper"
        request.ik_request.attempts = 20
        request.ik_request.pose_stamped.header.frame_id = "base"

        raw_input('Reach down: ')
        move(0.391, -0.326, 0.005, 0., 1., 0., 0., request)
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
            group = MoveGroupCommander("right_arm")

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
        #     group = MoveGroupCommander("right_arm")

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
        #     group = MoveGroupCommander("right_arm")

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
        #     group = MoveGroupCommander("right_arm")

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

