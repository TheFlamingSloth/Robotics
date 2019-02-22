import rospy
import numpy

class velocity:
    
    def __init__(self):
        
        self.vel_sub = rospy.Subscriber("/wheel_vel_left", float, self.callback)
        
    def callback(self, data):
        wheel_radius = .1
        robot_radius = 1

        c_l = wheel_radius * data
        c_r = wheel_radius * 0
        v = (c_l + c_r) / 2
        #a = (c_r - c_l) / (2 * robot_radius)
        self.geometry_msgs/Twist = v
        self.cmd_vel.publish(self.geometry_msgs/Twist)
        
        
rospy.init_node('velocity')
v = velocity()
rospy.spin()

#destroyAllWindows()