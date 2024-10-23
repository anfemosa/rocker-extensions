# workspace development helpers
RUN apt-get update \
  && apt-get install -y \
  # Base
  python3-colcon-common-extensions
  python3-vcstool
  python3-pip
  python3-venv
  # ROS tools
  ros-humble-rqt-controller-manager
  ros-humble-rqt-joint-trajectory-controller
  python3-bloom
  python3-rosdep
  fakeroot
  debhelper
  dh-python
  && apt-get clean
