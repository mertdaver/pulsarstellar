# Pulsar-Stellar's | C

### C Code for Robotics Library

This folder contains C code that is integrated into our Python robotics library. The reasons for using C in our project are as follows:

1. **Performance**: C is renowned for its performance and efficiency. We use C for the most performance-critical components of our library, including real-time sensor data processing and complex algorithmic computations.

2. **Compatibility with C Libraries**: Many powerful libraries in the robotics field are written in C. By using C, we can directly leverage these libraries without the need for wrappers or interfaces.

3. **Hardware Interaction**: C provides close-to-the-metal access to system resources, which is essential for direct hardware manipulation in robotics. This includes interactions with robot actuators, sensors, and other low-level hardware components.

4. **Concurrency and Real-time Processing**: C provides more direct control over threading and concurrency, which is crucial for real-time robotic applications. This allows us to manage parallel tasks more efficiently than Python.

5. **Memory Management**: In C, explicit memory management gives us fine-grained control over the resource allocation and optimization, essential for resource-constrained robotic systems.

Once the C code starts being used and specific compilers and dependencies are identified, they will be detailed in the CONTRIBUTING.md file.