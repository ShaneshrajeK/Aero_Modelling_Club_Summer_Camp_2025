<h1 align="center"><b>Advanced Control, Companion Computers & Swarm Fundamentals</b></h1>

---

## 1. How Does a Drone Stay Stable?

### 🌀 Control Hierarchy:

```text
Position Control
   ↓
Velocity Control
   ↓
Attitude Control (Pitch, Roll, Yaw)
   ↓
Rate Control (Angular Velocity)
```

* **Rate Loop**: Inner-most, runs fastest (\~400 Hz)
* **Attitude Loop**: Stabilizes orientation
* **Position Loop**: Uses GPS/optical flow to stay in place

> 📌 All of these loops use **PID controllers** — tuned separately

---

## 2. What is PID Control?

### ⚙️ PID = Proportional + Integral + Derivative

* **P (Proportional)**: Reacts to current error
* **I (Integral)**: Reacts to accumulated past error
* **D (Derivative)**: Reacts to rate of change of error

### PID Tuning Tips:

* Start with P → then D → finally I
* Use **simulators** to test
* Watch for overshoot, oscillation, or drift

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/77/PID_en.svg" width="60%">
</p>

---

## 3. Companion Computers 🧠

| **Device**                | **Use Case**                            |
| ------------------------- | --------------------------------------- |
| Raspberry Pi 4            | Lightweight processing (vision, MAVROS) |
| NVIDIA Jetson Nano/Xavier | GPU acceleration (AI, CV, ML)           |
| Intel NUC                 | Heavy processing, SLAM, autonomy        |

### Why use a Companion Computer?

* Onboard vision, navigation, or AI
* Offloading compute-heavy tasks from FCU
* Enabling **ROS**, **YOLO**, **SLAM**, etc.

### Typical Architecture:

```text
[FCU (Pixhawk)] ← MAVLink → [Jetson / Pi running ROS]
```

> 🔄 Use `MAVROS` to bridge ROS & PX4/ArduPilot

---

## 4. Non-GPS Navigation

### Alternatives to GPS:

| Tech                | Use For...           | Example             |
| ------------------- | -------------------- | ------------------- |
| **Optical Flow**    | Indoor stabilization | PX4Flow             |
| **Visual Odometry** | SLAM, CV navigation  | ORB-SLAM            |
| **Lidar/Depth**     | Obstacle avoidance   | RPLidar             |
| **UWB**             | Precise indoor loc   | Decawave            |
| **AprilTags/ArUco** | Precision landing    | Camera + Tag system |

<p align="center">
  <img src="https://raw.githubusercontent.com/PX4/PX4-user_guide/main/assets/peripherals/flow_px4flow_top.jpg" width="45%">
</p>

---

## 5. Intro to Swarm Drones 🐝

### What is a Swarm?

> A group of drones working **collaboratively**, usually with **decentralized coordination**.

### 🧠 Swarm Uses:

* Search & rescue
* Environmental monitoring
* Coordinated shows
* Redundant coverage

---

## 6. Types of Swarm Architectures

| Type              | Description                | Example Protocol |
| ----------------- | -------------------------- | ---------------- |
| **Centralized**   | One leader plans for all   | GCS controlled   |
| **Decentralized** | Each drone runs same logic | ROS 2 + DDS      |
| **Distributed**   | Peer-to-peer coordination  | V2V comms (UWB)  |

> 📡 Coordination can happen via Wi-Fi, UWB, or mesh radios

---

## 7. Multi-Drone with ROS + MAVROS

### 🚁 Multi-Drone Setup:

* Launch multiple **PX4 SITL** instances with different `SYSID`
* Connect to **MAVROS** on different namespaces
* Control each drone via ROS topics like:

```bash
/drone1/mavros/setpoint_position/local
/drone2/mavros/setpoint_position/local
```

### Launch File Example:

```xml
<group ns="drone1">
  <param name="fcu_url" value="udp://:14540@" />
</group>
<group ns="drone2">
  <param name="fcu_url" value="udp://:14541@" />
</group>
```

---

## 8. Tools for Swarm Simulation

| Tool                   | Feature                    |
| ---------------------- | -------------------------- |
| **Gazebo Multi-World** | Test multiple drones       |
| **AirSim + PX4**       | Vision + physics           |
| **ROS2 + CycloneDDS**  | Decentralized messaging    |
| **UWB Simulators**     | Emulate indoor positioning |

---

## 9. Challenges in Swarm Drones

* **Synchronization**: Time sync, coordinated execution
* **Collision Avoidance**: 3D path planning
* **Latency**: Communication delay in ROS or MAVLink
* **Scalability**: ROS 1 limits with more drones

> ✅ Future = ROS 2 + micro-ROS for onboard autonomy

---
