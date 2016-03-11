from lib import rospy
from msg_pack.std_msgs.msg import String
import env
def talker():
    rospy.init_node('talker', anonymous=True)

    pub = rospy.Publisher('chatter', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        str = String()
        str.data = hello_str
        rospy.loginfo(hello_str)
        pub.publish(str)
        rate.sleep()


talker()