from lib import rospy
from msg_pack.std_msgs.msg import String
import lib.env
import sys


# sys.argv+=["__master:=http://localhost:11411"]

def talker():
    rospy.init_node('talker', anonymous=False)

    pub = rospy.Publisher('chatter', String, queue_size=1)

    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        str = String()
        str.data = hello_str
        pub.publish(str)
        rate.sleep()


a = rospy.get_param("/s1/asd")
print(a)
#talker()
