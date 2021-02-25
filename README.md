
   <img src="https://user-images.githubusercontent.com/64838088/109208559-73860d00-77d0-11eb-84be-188b008e0aed.jpeg"/>

# Instructions to build `VMRC-v0`.


### Installation and Setup

* Clone the repository into your **root** folder.

      git clone https://github.com/southasia-marssociety/Virtual-Mars-Rover-Challenge-v0

* Create a folder called `src` in `Virtual-Mars-Rover-Challenge-v0/VMRC/ERDT/gym-gazebo/gym_gazebo/envs/installation/active_ws/`.

      cd ~/Virtual-Mars-Rover-Challenge-v0/VMRC/ERDT/gym-gazebo/gym_gazebo/envs/installation/active_ws/
      mkdir -p src

      
* Navigate into the `src` folder and paste your **world** and **rover** packages. 

<img src ="https://user-images.githubusercontent.com/64838088/109207314-002fcb80-77cf-11eb-8d6a-70f9506c9f7f.png"/>

* Copy the launch file that you want to launch and paste it in `Virtual-Mars-Rover-Challenge-v0/VMRC/ERDT/gym-gazebo/gym_gazebo/envs/assets/launch/`. 

<img src ="https://user-images.githubusercontent.com/64838088/109207622-58ff6400-77cf-11eb-8012-27281192f811.png"/>

* Navigate into the `Virtual-Mars-Rover-Challenge-v0/VMRC/ERDT/gym-gazebo/gym_gazebo/envs/TeamName/TeamName_rover.py` and make the following changes.

<img src ="https://user-images.githubusercontent.com/64838088/109208145-fa86b580-77cf-11eb-983a-ab29e3ea7532.png"/> 

* Build and install **gym-gazebo**.

      cd Virtual-Mars-Rover-Challenge-v0/VMRC/ERDT/gym-gazebo/
      sudo pip3 install -e .
      
* Load the environment variables corresponding to the robot you want to launch.

      cd Virtual-Mars-Rover-Challenge-v0/VMRC/ERDT/gym-gazebo/gym_gazebo/envs/installation/
      bash setup_noetic.bash
      
* Execute the test script.

      cd Virtual-Mars-Rover-Challenge-v0/VMRC/ERDT/gym-gazebo/examples/TRAINING-SCRIPT/
      python3 test.py
      

