import os, sys

sys.path
path = os.path.dirname(os.getcwd())
ros_env = {
    'ROS_PACKAGE_PATH': path + '\\msg_pack',
    'ROS_MASTER_URI': 'http://localhost:11311',
    'ROS_PYTHON_LOG_CONFIG_FILE': path + '\\etc\\python_logging.conf',
    'PYTHONPATH': path + '\\lib'
}
for i in ros_env:
    os.environ[i] = ros_env[i]