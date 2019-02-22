import rospy
from std_msgs.msg import String

rospy.init_node('publisher', anonymous=True)


p = rospy.Publisher('/foo', String, queue_size=1)

while not rospy.is_shutdown():
    text = String()
    text.data = 'hello world'
    p.publish(text)
    print 'published text'
    rospy.sleep(1)