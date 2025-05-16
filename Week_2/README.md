# Week 2: Into the Software


<h1 align="center"><b>Simulation, Software & Autonomy</b></h1>

---

## 1. Why Simulate?

### 🧠 Before flying in real life…

* Simulations allow safe testing of:

  * Autopilot behavior
  * PID tuning
  * Mission planning
  * Sensor performance

> ✅ Train like a pro, crash virtually (not physically)

---

## 2. Popular Drone Simulators

| **Simulator**          | **Use Case**           | **Strengths**                                |
| ---------------------- | ---------------------- | -------------------------------------------- |
| **Gazebo + PX4**       | Research, ROS          | Realistic physics, MAVROS, SITL              |
| **AirSim (Microsoft)** | AI, computer vision    | Unreal Engine graphics, APIs for ML training |
| **Liftoff**            | FPV Racing             | Realistic FPV physics, racing drone practice |
| **Velocidrone**        | FPV, Acro              | Low-latency simulation, tracks & multiplayer |
| **RealFlight**         | General drone training | RC-like interface, multiple aircraft types   |

<p align="center">
  <img src="https://raw.githubusercontent.com/PX4/PX4-user_guide/main/assets/simulation/px4-gazebo-sitl-diagram.png" width="70%">
</p>

---

## 3. SITL & HITL

| Type     | Description                                         | Hardware Needed |
| -------- | --------------------------------------------------- | --------------- |
| **SITL** | Software-In-The-Loop (e.g. PX4 + Gazebo)            | ❌               |
| **HITL** | Hardware-In-The-Loop (real flight controller + sim) | ✅               |

> 🧪 Use SITL to test code and control algorithms before trying them on a real drone.

---

## 4. MAVLink: Drone Communication Protocol

### 🛰️ What is MAVLink?

* **Micro Air Vehicle Link**: lightweight, header-only communication protocol
* Standard for **autonomous drones**

### 🔗 MAVLink Enables:

* GCS ↔ Drone communication
* Sensor data transmission
* Mission upload/download
* Telemetry (GPS, IMU, battery, etc.)

> Libraries: `pymavlink`, `mavros`, `mavsdk`

<p align="center">
  <img src="https://raw.githubusercontent.com/mavlink/mavlink/master/logo/mavlink-logo.png" width="100">
</p>

---

## 5. Ground Control Station (GCS) Software

| **Tool**                    | **Platform**   | **Used With**           |
| --------------------------- | -------------- | ----------------------- |
| **Mission Planner**         | Windows        | ArduPilot               |
| **QGroundControl**          | Cross-platform | PX4 & ArduPilot         |
| **APM Planner 2**           | Linux/Mac      | ArduPilot               |
| **Betaflight Configurator** | Chrome App     | Betaflight (FPV drones) |

### 🧭 Common GCS Features:

* Live telemetry view (altitude, GPS, battery, etc.)
* Sensor calibration
* Waypoint mission planning
* Firmware flashing
* Parameter tuning

---

## 6. Creating an Autonomous Mission

### 📋 Typical Mission:

1. **Takeoff** to a defined altitude
2. Fly through **waypoints**
3. Perform **actions** (photo, hover, drop)
4. **Return to Launch (RTL)**

### Example (Mission Planner):

```plaintext
WAYPOINT 1: TAKEOFF (10m)
WAYPOINT 2: FLY TO GPS X,Y
WAYPOINT 3: DO_ACTION
WAYPOINT 4: RTL
```

<p align="center">
  <img src="https://ardupilot.org/copter/_images/mission-planner-flight-plan-tab.jpg" width="70%">
</p>

---

## 7. ROS Integration with PX4

### 🤖 Why Use ROS?

* Modular, flexible robotics framework
* Ideal for swarm drones, computer vision, SLAM, etc.

### Common Tools:

* `mavros`: MAVLink ↔ ROS bridge
* `rqt`: GUI for plotting & debugging
* `rosbag`: Data recording
* `rviz`: 3D visualization

### Typical Setup:

```
[QGroundControl] ← MAVLink → [PX4 SITL] ← MAVROS → [ROS Nodes]
```

> 🛠️ Try simple scripts in `Python` using `rospy` + `mavros_msgs`.

---

## 8. Workflow: From Code to Sky 🌤️

| Step                     | Tools Used                       |
| ------------------------ | -------------------------------- |
| 1. Develop control logic | PX4 / ArduPilot + C++/Python     |
| 2. Simulate & test       | Gazebo, AirSim, SITL             |
| 3. Monitor in GCS        | QGroundControl / Mission Planner |
| 4. Flash firmware & fly  | Pixhawk / Flight Controller      |
| 5. Analyze logs          | `.tlog` / `.bin` in GCS          |

---

## 9. Glossary

* **SITL**: Software-in-the-loop simulation
* **MAVLink**: Standard drone communication protocol
* **GCS**: Ground Control Station
* **Waypoint**: Predefined GPS location in mission
* **QGC**: QGroundControl
* **ROS**: Robot Operating System

---

# Next: [ROS2 Installation](https://github.com/ShaneshrajeK/Aero_Modelling_Club_Summer_Camp_2025/blob/main/Week_2/ros2.md)

---
