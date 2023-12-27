# Pulsar-Stellar's | C++

### C++ Code for Robotics Library

This folder contains C++ code that is integrated into our Python robotics library. The reasons for using C++ in our project are as follows:

1. **Performance**: C++ is generally faster than Python. We use C++ for performance-critical parts of our library, such as real-time sensor data processing or complex calculations.

2. **Existing C++ Libraries**: We leverage powerful C++ libraries available for robotics, such as possibly ROS (Robot Operating System), PCL (Point Cloud Library), and OpenCV.

3. **Hardware Interaction**: C++ provides lower-level access to system resources than Python. We use C++ for direct interactions with hardware, such as robot actuators or sensors.

4. **Multithreading**: Python has some limitations when it comes to multithreading due to the Global Interpreter Lock (GIL). C++ does not have this limitation, so we use it for tasks that need to be performed in parallel.

Once C++ starts being used and have specified specific compilers and dependencies, they will be specified in CONTRIBUING.md file, we just need a C++ dev first to help lol.

