import rospy
import time
import rospkg

from gazebo_msgs.msg import LinkStates
from std_srvs.srv import Empty
from gym import utils, spaces
from gym_gazebo.envs import gazebo_env

from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState
from tf2_geometry_msgs import PoseStamped
rospack = rospkg.RosPack()

class TeamNameEnv(gazebo_env.GazeboEnv):

    def __init__(self):

        gazebo_env.GazeboEnv.__init__(self, "leo_marsyard.launch")

        self.reward = 0
        #self.observation_space = spaces.Box(-inf, inf, shape=(3,), dtype=np.float32)
        #self.action_space = spaces.Box(-0.34, 0.524, shape=(4,), dtype=np.float32)

        self.package_path = rospack.get_path('leo_simulator')


        self.pause = rospy.ServiceProxy("/gazebo/pause_physics", Empty)
        self.unpause = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
        self.reset_proxy = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
        
        self.rate = rospy.Rate(50)
