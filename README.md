# Requirements

1) Ubuntu 12.04 or higher (tested with 16.04)

Python requirements to install Sphero driver:

    sudo apt install python-pip python-dev ipython
    sudo apt install bluetooth libbluetooth-dev
    sudo pip install pybluez
    pip install --upgrade
    sudo apt install python-catkin-pkg


# Build and install driver
(Repeat again later if you want to apply changes to the driver code)

    cd sphero_driver
    python setup.py build
    sudo python setup.py install


Install ROS version matching your Ubuntu version

    see ros.org