import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# Gazebo
# ----------------------------------------


register(
    id='GazeboMarsTeamNameForce-v0',
    entry_point='gym_gazebo.envs.TeamName:TeamNameEnv',
)


