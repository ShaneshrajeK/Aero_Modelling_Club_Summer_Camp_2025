# **Computer Vision and Visual SLAM (VSLAM)**

### 📌 **Overview**

As drones increasingly operate in GPS-denied environments (indoor, urban canyons, tunnels), **Computer Vision** becomes a critical enabler of autonomy. One of the most powerful techniques for spatial awareness in such scenarios is **Visual SLAM (Simultaneous Localization and Mapping)** — where the drone builds a map of an unknown environment while simultaneously localizing itself within it using camera input.

---

### 🎯 **Goals of VSLAM in Drones**

* Navigate autonomously without GPS
* Build 3D maps of the environment
* Avoid obstacles and re-localize after drift
* Enable high-level AI tasks (search and rescue, inspection, etc.)

---

## 🧠 1. **What is SLAM?**

SLAM is the process of:

* **Mapping**: Creating a 2D or 3D map of the environment
* **Localization**: Determining the drone’s position within that map

**VSLAM** uses cameras (monocular, stereo, or RGB-D) to perform SLAM, often aided by IMUs for improved robustness.

---

## 📷 2. **Types of Visual SLAM in Drones**

| Type        | Description                          | Use-case                                  |
| ----------- | ------------------------------------ | ----------------------------------------- |
| Monocular   | Single camera                        | Lightest, but scale is ambiguous          |
| Stereo      | Two cameras (depth from disparity)   | Better scale estimation, ideal for drones |
| RGB-D       | RGB + Depth sensor (e.g., Realsense) | Dense maps, best indoors                  |
| Event-based | High-speed dynamic scenes            | FPV, racing, aggressive maneuvers         |

---

## 🔍 3. **Core Pipeline of VSLAM**

Here's what happens step-by-step inside a VSLAM system:

1. **Image Acquisition**: Capture frames from camera(s)
2. **Feature Extraction**: Detect keypoints (e.g., ORB, FAST)
3. **Feature Matching**: Match features between frames
4. **Pose Estimation**: Estimate motion using epipolar geometry or PnP
5. **Map Update**: Triangulate landmarks and update map
6. **Loop Closure**: Recognize previously seen locations to correct drift
7. **Bundle Adjustment**: Optimize camera poses and map points globally

---

## 🧪 4. **Popular Open-Source VSLAM Libraries**

| Library       | Description                           | Notes                                 |
| ------------- | ------------------------------------- | ------------------------------------- |
| **ORB-SLAM3** | Robust monocular, stereo, RGB-D VSLAM | Lightweight and ROS-compatible        |
| **RTAB-Map**  | Real-time appearance-based mapping    | Supports stereo, RGB-D, LiDAR         |
| **LSD-SLAM**  | Direct monocular SLAM                 | Good for low-texture environments     |
| **OpenVSLAM** | Modular and versatile                 | Supports multiple camera models       |
| **Kimera**    | VIO + VSLAM + Mesh reconstruction     | Advanced, good for mapping + planning |

All of these have ROS1/ROS2 support, with prebuilt examples for drones using MAVROS and PX4.

---

## 🧰 5. **Hardware for Visual SLAM on Drones**

| Component           | Options                                     | Notes                                   |
| ------------------- | ------------------------------------------- | --------------------------------------- |
| **Cameras**         | Raspberry Pi Cam, ZED Mini, Intel Realsense | Stereo or RGB-D preferred               |
| **IMU**             | MPU9250, BMI088, built-in flight controller | Required for Visual-Inertial SLAM (VIO) |
| **Computing**       | Raspberry Pi 5, Jetson Nano/Xavier, OAK-D   | Onboard inference or edge streaming     |
| **Synchronization** | Hardware sync or software time alignment    | Crucial for VIO stability               |

---

## ⚙️ 6. **Software Stack and ROS Integration**

To deploy VSLAM on a drone:

1. **Sensor Drivers**:

   * `usb_cam` / `realsense2_camera` / `zed_ros2_wrapper`

2. **SLAM Node**:

   * `rtabmap_ros` or `orb_slam3_ros`

3. **Pose Publisher**:

   * Publishes `/tf` or `/odom` for flight controller

4. **Flight Stack**:

   * PX4 + MAVROS, or ArduPilot + MAVLink

5. **Mapping/Visualization**:

   * Use RViz or WebRTC-based UIs

6. **Optional**:

   * `robot_localization` for sensor fusion
   * `octomap_server` for 3D occupancy mapping

---

## 🛰️ 7. **Use Cases in Drone Applications**

| Application             | How VSLAM Helps                                  |
| ----------------------- | ------------------------------------------------ |
| **Indoor Navigation**   | Replace GPS, avoid walls, maintain map           |
| **Autonomous Delivery** | Dynamic re-routing in urban zones                |
| **Search & Rescue**     | Map unknown buildings, find survivors            |
| **Agriculture**         | Plant-level inspection in GPS-denied greenhouses |
| **Drone Swarms**        | Collaborative mapping and localization           |

---

## ⚖️ 8. **Comparison with Other Techniques**

| Technique           | Pros                      | Cons                                 |
| ------------------- | ------------------------- | ------------------------------------ |
| **GPS-based**       | Simple, scalable          | Fails indoors or in GPS-denied areas |
| **LiDAR SLAM**      | High accuracy             | Expensive, power-heavy               |
| **VSLAM**           | Lightweight, camera-based | Sensitive to lighting, texture       |
| **Visual-Inertial** | Robust to motion blur     | Needs good IMU integration           |

---

## 🧩 9. **Challenges in Real-World Deployment**

* Vibration from rotors → use dampers or EKF filters
* Lighting changes → use adaptive exposure, direct SLAM
* Textureless environments → rely on depth sensors or hybrid SLAM
* Compute constraints → offload to ground or use edge TPUs
* Loop closure in large areas → visual vocabulary trees or cloud maps

---

## 🔗 10. **Further Exploration**

* Explore **Kimera-VIO** for high-quality VSLAM + mesh reconstruction
* Try integrating **RTAB-Map + Realsense + MAVROS** in a simulation (Gazebo/Ignition)
* Experiment with **OpenVINS** for lightweight onboard SLAM
* Use **AirSim** or **UAVSim** to simulate GPS-denied scenarios

---

## 🧠 TL;DR

Visual SLAM enables drones to **"see" and "remember"** their environment — replacing GPS with vision for indoor, dynamic, and complex environments. Whether you're working on palm-sized indoor bots or large autonomous flyers, integrating computer vision with IMU and robust SLAM algorithms is key to next-gen autonomy.

---

