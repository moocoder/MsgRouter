
import rosmaster
import os,sys
ros_env = {
    'ROS_PACKAGE_PATH': 'f:\\temp\\ros',
    'ROS_MASTER_URI': 'http://localhost:11311',
    'ROS_PYTHON_LOG_CONFIG_FILE': 'F:\\temp\etc\\ros\\python_logging.conf'
}
for i in ros_env:
    os.environ[i]=ros_env[i]
if __name__ == "__main__":
    rosmaster.rosmaster_main(sys.argv)