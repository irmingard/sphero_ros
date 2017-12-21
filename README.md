# Setup

1) Install Ubuntu 16.04

2) Install the following dependencies
    
    ```
    sudo apt install python-pip python-dev ipython
    sudo apt install bluetooth libbluetooth-dev
    sudo pip install pybluez
    pip install --upgrade
    sudo apt install python-catkin-pkg
    ```
        
3) Install ROS Kinetic Kame following the instructions here

    http://wiki.ros.org/kinetic/Installation/Ubuntu

4) Run the following to build and install the Sphero Python driver
(Repeat again later if you want to apply changes to the driver code)


    cd sphero_driver
    python setup.py build
    sudo python setup.py install
