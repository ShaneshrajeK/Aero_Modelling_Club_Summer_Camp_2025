<h1 align = "center"><b> 🚁 Drone 101</b></h1>

---

## 1. Drone Aerodynamics

Multirotor drones fly by generating lift through spinning rotors. Understanding the basics of drone aerodynamics is key to mastering UAV design and control.

### 📌 The Four Forces of Drone Flight

<p align="center">
  <img src="https://cfdflowengineering.com/wp-content/uploads/2020/09/Drone_cove-page.png" width="50%">
</p>

1. **Weight (Gravity)**
   Pulls the drone toward the Earth. Acts through the center of gravity (CG). Battery, frame, motors, and payload contribute to total mass.

2. **Lift**
   Produced by spinning propellers. Each rotor generates lift by accelerating air downward. For a stable hover, total lift = weight.

3. **Thrust**
   In multirotors, thrust and lift are the same (vertical). In forward flight, a tilt causes part of the thrust vector to become horizontal, propelling the drone.

4. **Drag**
   Air resistance acting opposite to the drone’s motion. Affects forward flight and increases with speed and surface area.

---

### 🌀 How Multirotors Fly: The Physics

<p align="center">
  <img src="https://i.sstatic.net/fbjwb.jpg" width="60%">
</p>

* Drones like quadcopters have **fixed-pitch rotors**.
* Control is achieved by **varying motor speeds**.
* Each rotor spins clockwise (CW) or counterclockwise (CCW) to balance torque.

| **Motion**                    | **How It's Achieved**                                            |
| ----------------------------- | ---------------------------------------------------------------- |
| **Hover**                     | All rotors spin at the same speed, lift = weight.                |
| **Climb/Descend**             | Increase/decrease all rotor speeds equally.                      |
| **Pitch (Tilt Forward/Back)** | Increase rear motor speed, decrease front motor (or vice versa). |
| **Roll (Tilt Left/Right)**    | Increase right-side motors, decrease left (or vice versa).       |
| **Yaw (Turn CW/CCW)**         | Adjust opposite-pair motor speeds to create unbalanced torque.   |

---

### ⚙️ Propellers and Lift Generation

<p align="center">
  <img src="https://blog.platypush.tech/img/propeller-schema.png" width="40%">
</p>

* Propellers act like rotating airfoils.
* Lift depends on:

  * **RPM (Rotations per Minute)**
  * **Blade shape and pitch**
  * **Diameter and number of blades**
* **CW and CCW propellers** cancel out torque to avoid uncontrolled yaw.

---

## 2. Parts of a Drone

<p align="center">
  <img src="https://pub.mdpi-res.com/drones/drones-07-00268/article_deploy/html/images/drones-07-00268-g005.png?1681383992" width="40%">
</p>

--- 

### 🔧 1. Frame

The structural skeleton holding all parts together. Materials: Carbon fiber (light & strong), plastic (cheap), aluminum.

<p align="center">
  <img src="https://roboticsbiz.com/wp-content/uploads/2019/05/frames.jpg" width="60%">
</p>

---

### 🔧 2. Propellers

Create lift. Must be balanced. Typically two CW and two CCW in quadcopters.

<p align="center">
  <img src="https://learnassets.getfpv.com/learn/wp-content/uploads/2018/01/05182004/3-Prop-Blades.jpg" width="60%">
  <img src="https://img-new.cgtrader.com/items/4334861/bf011f7ba9/large/toroidal-propeller-3d-model-bf011f7ba9.jpg" width="35%">
</p>

---

### 🔧 3. Motors

Brushless DC motors (BLDC) are preferred for power and reliability. Paired with Electronic Speed Controllers (ESCs).

<p align="center">
  <img src="https://i.pinimg.com/736x/fd/9f/de/fd9fde3b6ae32b07bc1114699f3c1530.jpg" width="50%">
</p>

---

### 🔧 4. ESCs (Electronic Speed Controllers)

Control motor speed based on signals from flight controller.

<p align="center">
  <img src="https://www.engineersgarage.com/wp-content/uploads/2023/05/DroneESCrotator.png" width="60%">
</p>

---

### 🔧 5. Battery

Usually Li-Po (Lithium-Polymer). 

<p align="center">
  <img src="https://www.remoteflyer.com/wp-content/uploads/2022/08/drone-battery-header-e1659950722450.jpg" width="70%">
</p>

Ratings:
* **Voltage (V)** – number of cells (3S = 11.1V)
* **Capacity (mAh)** – total energy storage
* **C-rating** – how quickly energy can be discharged

---

### 🔧 6. Flight Controller

The drone’s brain. Interprets pilot inputs and sensor data to control ESCs.

<p align="center">
  <img src="https://rcdrone.top/cdn/shop/articles/PixhawkFamily.jpg?v=1730607031" width="50%">
</p>

Popular FCs:

* **Pixhawk**
* **Speedybee**
* **Betaflight / INAV**
* **DJI Naza / A3**

---

### 🔧 7. GPS Module

Provides position hold, return-to-home (RTH), and autonomous navigation.

<p align="center">
  <img src="https://oscarliang.com/wp-content/uploads/2023/03/fpv-drone-gps-module-betaflight-inav-rescue-return-to-home-round-up-testing.jpg" width="50%">
</p>

---

### 🔧 8. IMU (Inertial Measurement Unit)

Contains accelerometers and gyros. Measures orientation and motion.

<p align="center">
  <img src="https://www.mdpi.com/drones/drones-08-00738/article_deploy/html/images/drones-08-00738-g001.png" width="60%">
</p>

---

### 🔧 9. Barometer

Measures air pressure to determine altitude.

<p align="center">
  <img src="https://ardupilot.org/copter/_images/baro-ms5611-pixhawk.jpg" width="50%">
</p>

---

### 🔧 10. Camera and Gimbal

Used for FPV (First Person View), mapping, or surveillance. Gimbals stabilize footage.

<p align="center">
  <img src="https://www.unmannedsystemstechnology.com/wp-content/uploads/2020/01/Gremsy-T3-PE-drone-camera-gimbal-1024x683.jpg" width="50%">
</p>

---

### 🔧 11. Telemetry & RF Modules

Send data (GPS, battery, altitude) to ground station. Optional RC or 4G/5G control.

<p align="center">
  <img src="https://m.media-amazon.com/images/I/71fUVx6oqvL._AC_UF1000,1000_QL80_.jpg" width="50%">
  <img src="https://m.media-amazon.com/images/I/61jBKSlM4AL.jpg" width="37.6%">
</p>

---


## Types of Drones by Configuration

| **Type**                | **Description**                            | **Use Case**                                  |
| ----------------------- | ------------------------------------------ | --------------------------------------------- |
| **Tricopter**           | 3 motors, more agile but less stable       | Hobby use, experimental builds                |
| **Quadcopter (X or +)** | 4 motors, most common, balanced and simple | Aerial imaging, inspection, mapping           |
| **Hexacopter**          | 6 motors, higher lift and redundancy       | Heavy-lift, commercial use                    |
| **Octocopter**          | 8 motors, extremely stable and reliable    | Professional cinematography, industrial tasks |

---

# Types, Control, and Autonomy of Drones

---

## 1. Drone Classifications

### 🔹 Based on **Weight** (India - DGCA)

| **Category** | **Weight**     | **Example Use**                   |
| ------------ | -------------- | --------------------------------- |
| Nano         | < 250 g        | Toy drones, mini FPV quads        |
| Micro        | 250 g – 2 kg   | Hobby flying, small camera drones |
| Small        | 2 kg – 25 kg   | Survey drones, delivery drones    |
| Medium       | 25 kg – 150 kg | Agriculture, mapping, logistics   |
| Large        | > 150 kg       | Military, cargo transport         |

> 🎯 *Note: DGCA registration and UIN (Unmanned Aircraft Operator Permit) required for drones > 250g*

---

## 2. Drone Communication Systems

<p align="center">
  <img src="https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs42452-020-2749-5/MediaObjects/42452_2020_2749_Fig1_HTML.png" width="60%">
</p>

### 🎮 **Radio Control (RC)**

Traditional method using handheld transmitter and receiver (e.g., FrSky, FlySky, DJI controllers).

* 2.4 GHz or 5.8 GHz frequency bands
* 4+ channels (Throttle, Roll, Pitch, Yaw)

---

### 📡 **Telemetry Communication**

Links drone to Ground Control Station (GCS) for monitoring and mission planning.

* **915 MHz / 433 MHz telemetry modules** (SiK radio)
* Shows battery, GPS, altitude, RC signal, etc.
* Software: Mission Planner, QGroundControl

---

### 🌐 **4G/5G and WiFi Drones**

Used in advanced UAVs (custom or DJI Enterprise). Enables:

* BVLOS (Beyond Visual Line of Sight) control
* Real-time data streaming
* Cloud integration

---

## 3. First Person View (FPV)

<p align="center">
  <img src="https://i.ytimg.com/vi/9DY9Cn8Ld_A/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBuUP17vWfsjfmimKJytIi8ktS53Q" width="60%">
</p>

### 📹 **What is FPV?**

Live video feed from the drone’s onboard camera to pilot goggles or screen.

### 🔧 Components:

| **Component**           | **Function**                         |
| ----------------------- | ------------------------------------ |
| FPV Camera              | Captures live view (low latency)     |
| VTx (Video Transmitter) | Sends video over analog/digital link |
| VRx (Video Receiver)    | On goggles or ground station         |
| Goggles/Monitor         | Displays real-time video             |

> 🎯 *FPV racing drones prioritize latency and maneuverability.*

---

## 4. Sensors for Autonomy

| **Sensor**             | **What It Measures**       | **Used For**                            |
| ---------------------- | -------------------------- | --------------------------------------- |
| **IMU**                | Orientation & motion       | Stabilization, attitude control         |
| **GPS**                | Global position            | Waypoints, RTH, geo-fencing             |
| **Barometer**          | Altitude (pressure-based)  | Alt-hold, terrain following             |
| **Magnetometer**       | Compass heading            | Yaw reference, autonomous nav           |
| **Lidar / Sonar**      | Distance to ground/objects | Obstacle avoidance, landing             |
| **Optical Flow / VIO** | Movement across surfaces   | Position hold indoors, GPS-denied areas |

---

## 5. Levels of Drone Autonomy

| **Autonomy Level**       | **Description**                                                           |
| ------------------------ | ------------------------------------------------------------------------- |
| **Manual**               | Full control via RC; pilot adjusts every axis                             |
| **Stabilized**           | Assisted by gyros and accelerometers; keeps level                         |
| **Altitude Hold**        | Barometer/IMU maintain fixed height                                       |
| **GPS Hold / Loiter**    | Drone hovers at a fixed GPS position                                      |
| **Return to Home (RTH)** | Automatically returns to takeoff point if triggered                       |
| **Waypoint Mission**     | Predefined GPS path using GCS (e.g., Mission Planner)                     |
| **Full Autonomy**        | Obstacle-aware, adaptive route planning, swarm coordination, AI decisions |

---

### 🗺️ Example: Waypoint Mission Planning

<p align="center">
  <img src="https://docs.qgroundcontrol.com/Stable_V4.3/assets/plan_view_overview.DwcNZe50.jpg" width="60%">
</p>

Software like **Mission Planner** or **QGroundControl** lets you:

* Upload mission with GPS waypoints
* Define altitude, speed, camera actions
* View telemetry in real time
* Monitor drone health and logs

---

## 6. Failsafe and Redundancy

### 🔐 Failsafes (in Pixhawk/Ardupilot systems):

* **Low Battery Failsafe:** Land or RTL
* **GPS Loss Failsafe:** Switch to Alt-hold
* **RC Signal Loss:** Hover / RTL / Land
* **Geofence Breach:** RTL or Terminate

> 🛡️ Always test failsafes before an autonomous mission.

---

## 7. Indian Drone Regulations Snapshot (2025)

### ✅ You *must* follow:

* **UIN (Registration)** for drones > 250g
* **Drone Pilot Training (Micro and above)** if used commercially
* **NPNT Compliance:** No-Permission No-Takeoff (DGCA)
* **Geo-fencing:** No flying near airports, military areas
* **Max altitude for micro drones:** 60m (AGL)

### Resources:

* [Digital Sky Platform (DGCA)](https://digitalsky.dgca.gov.in)
* [UAS Rules 2021 PDF](https://egazette.nic.in)

---

# Drone Hardware, Assembly & PID Tuning

---

## 1. Drone Subsystems Overview

<p align="center">
  <img src="https://www.mdpi.com/sensors/sensors-24-03064/article_deploy/html/images/sensors-24-03064-g001-550.jpg" width="75%">
</p>

### Key Subsystems:

| **Subsystem**     | **Main Components**                          |
| ----------------- | -------------------------------------------- |
| **Power**         | LiPo Battery, PDB, Voltage Regulators (BECs) |
| **Propulsion**    | Motors (BLDC), ESCs, Propellers              |
| **Control**       | Flight Controller (FC), RC Receiver, Sensors |
| **Communication** | RC Tx/Rx, Telemetry Module, FPV system       |
| **Navigation**    | GPS Module, Magnetometer, IMU                |
| **Structure**     | Frame, Landing Gear, Mounts                  |

---

## 2. Electronic Speed Controllers (ESCs)

### 🔧 What They Do:

* Convert throttle signals into motor speed by varying voltage.
* Support **PWM**, **OneShot**, **DShot** protocols.
* Firmware: **BLHeli**, **SimonK**

> 🌀 Choose ESC rating based on max motor current (e.g., 30A ESC for 2212 motors).

---

## 3. BLDC Motors & Propellers

### 🔩 Motor Naming (Example: 2212 1000KV)

* **22**: Stator diameter (mm)
* **12**: Stator height (mm)
* **1000KV**: RPM per volt input

### ⚙️ Propeller Sizing

* Format: *Diameter x Pitch* (e.g., 10x4.5)
* Material: Plastic, Carbon fiber
* Use CW and CCW pairs for quadcopters.

> 🎯 Match motor + prop + battery for thrust > 2× total drone weight (for safe flight).

---

## 4. Choosing the Right Frame

| **Frame Type**    | **Use Case**                          |
| ----------------- | ------------------------------------- |
| X-Frame           | FPV racing, agility                   |
| H-Frame           | Payload drones, more space            |
| Deadcat           | Aerial photography (no props in view) |
| V-Tail / Y6 / Hex | Redundancy, stability                 |

> Material: Carbon Fiber (lightweight & strong), Plastic (beginner builds)

---

## 5. Building Your First Drone: Assembly Guide

### 🧰 Basic Components:

* Flight Controller (Pixhawk / KK2 / F4)
* 4× Motors (e.g., 2212)
* 4× ESCs (30A)
* LiPo Battery (3S/4S 2200–5200mAh)
* Frame (450mm for starters)
* GPS module (optional)
* RC Tx/Rx (FlySky i6, Taranis QX7, etc.)
* Power Distribution Board (PDB)
* Propellers (e.g., 10x4.5)
* Mounts, vibration dampeners

### 🛠️ Build Order:

1. Assemble the frame
2. Mount motors and ESCs
3. Solder PDB → ESCs → Motors
4. Mount Flight Controller (with vibration isolation)
5. Connect RC Receiver
6. Install GPS, buzzer, LEDs (optional)
7. Calibrate via GCS (Mission Planner / Betaflight)


---

## 6. Thrust-to-Weight Ratio (TWR)

### Why It Matters:

* For a drone to take off, total thrust > total weight.

### 🔍 Calculation:

If each motor produces 1 kg thrust, and your drone weighs 1.5 kg:

* **Total Thrust = 4 kg**
* **TWR = 4 / 1.5 = 2.66**
  ✅ Good TWR for stability and performance.

| **Application**    | **Recommended TWR** |
| ------------------ | ------------------- |
| Stable Photography | \~2:1               |
| Racing / Acro      | >4:1                |
| Heavy Lift / VTOL  | >2.5:1              |

---

## 7. PID Tuning Basics

### 🔁 What is PID?

PID = **Proportional**, **Integral**, **Derivative**
Used in flight controllers to maintain stability.



### 🎚️ Parameters:

| Term  | Effect on Flight                                                          |
| ----- | ------------------------------------------------------------------------- |
| **P** | Reacts to current error (too low = slow response, too high = oscillation) |
| **I** | Reacts to accumulated error (useful for wind drift correction)            |
| **D** | Reacts to rate of error change (adds damping)                             |

> 🔧 Tools: Betaflight Configurator, Mission Planner
> 🧪 Method: Adjust one axis at a time, test in hover

---

## 8. Firmware Comparison

| Feature           | **ArduPilot**             | **PX4**                | **Betaflight**          |
| ----------------- | ------------------------- | ---------------------- | ----------------------- |
| **Use case**      | Professional / research   | Robotics, dev-friendly | FPV & freestyle         |
| **GCS support**   | Mission Planner, QGC      | QGroundControl         | Betaflight Configurator |
| **Autonomy**      | ✅ Waypoints, RTH, MAVLink | ✅ ROS compatible       | ❌ Manual only           |
| **Flexibility**   | Very high                 | High                   | Limited                 |
| **Target boards** | Pixhawk, APM, Cube, etc.  | Pixhawk, Holybro, etc. | F3, F4, F7, H7 FCs      |
| **Community**     | Huge                      | Developer focused      | FPV racing focus        |

---

## 9. Safety & Best Practices

* ✅ Calibrate sensors before every flight
* ✅ Check CG (center of gravity)
* ✅ Isolate vibrations (especially for barometer & IMU)
* ✅ Set failsafes (RC loss, GPS loss, low battery)
* ✅ Test hover indoors before outdoor flight
* ✅ Respect local laws & fly in open spaces

---
