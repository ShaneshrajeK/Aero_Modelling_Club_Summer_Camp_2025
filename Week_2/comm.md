<h1 align="center"><b>Drone Communication & Networking</b></h1>

---

## 1. Why Communication Matters

Communication is essential for:

* **Control** (manual or autonomous)
* **Telemetry** (health, location, sensor data)
* **Video streaming**
* **Swarm coordination**
* **Remote mission uploads**

> 📡 Drone communication = backbone of autonomy

---

## 2. Types of Communication Links

| Link Type          | Purpose                      | Common Protocols     |
| ------------------ | ---------------------------- | -------------------- |
| **RC Link**        | Pilot → Drone control        | PWM, PPM, SBUS, CRSF |
| **Telemetry**      | Bi-directional data exchange | MAVLink, SiK         |
| **FPV Video**      | Live video feed              | Analog, DJI, HDZero  |
| **Companion Link** | FCU ↔ Companion Computer     | MAVLink (UART/USB)   |
| **Drone↔Drone**    | Swarm coordination           | Wi-Fi, UWB, ESP-NOW  |

---

## 3. RC Protocols

### 🚀 Traditional:

* **PWM/PPM**: Simple, old-school
* **SBUS**: Low latency, digital (Futaba, FrSky)

### ⚡ Modern:

* **CRSF (Crossfire)**: Low latency, long range (TBS)
* **ELRS (ExpressLRS)**: Open-source, ultra-low latency (up to 30km)

| Protocol | Latency  | Range     | Open-source |
| -------- | -------- | --------- | ----------- |
| PWM      | High     | Low       | Yes         |
| SBUS     | Medium   | Medium    | No          |
| ELRS     | Very Low | Very High | ✅           |

---

## 4. Telemetry Radios

### 🛰️ Common Radios:

* **3DR SiK Radios** (433/915 MHz)
* **RFD900x**: Long range (40 km+)
* **ESP32**: Wi-Fi link (custom scripts)

### Typical Setup:

```text
GCS ←→ USB Telemetry Radio ←→ SiK Radio ←→ Pixhawk TELEM1
```

### Telemetry Use:

* Send **MAVLink** commands
* View data in **QGroundControl** or **Mission Planner**

---

## 5. Video Transmission

| System         | Type    | Pros                          | Cons          |
| -------------- | ------- | ----------------------------- | ------------- |
| **Analog FPV** | 5.8 GHz | Low latency, cheap            | Poor quality  |
| **DJI FPV**    | Digital | HD video, low latency (28 ms) | Cost, closed  |
| **HDZero**     | Digital | Open digital FPV              | Limited range |

> 🎥 DJI FPV is common in professional autonomous and racing drones.

---

## 6. Companion Computer ↔ FCU

### 📡 Communication:

* Use **UART** or **USB**
* Protocol: **MAVLink**
* Bridging via **MAVROS**, **DroneKit**, **pymavlink**

```bash
roslaunch mavros px4.launch fcu_url:=/dev/ttyUSB0:57600
```

> Ensure **flow control** (TX/RX/GND), proper **baud rate**.

---

## 7. Drone-to-Drone Communication

### 🤝 Peer-to-Peer Links:

| Method             | Protocol    | Use Case                    |
| ------------------ | ----------- | --------------------------- |
| **Wi-Fi**          | TCP/UDP     | ROS topics, MAVLink         |
| **UWB (Decawave)** | TWR/TDOA    | Indoor positioning, ranging |
| **ESP-NOW**        | Proprietary | Low-power mesh comms        |
| **nRF Mesh**       | BLE Mesh    | Basic swarm comms           |

### Common Config:

* Assign each drone an IP (Wi-Fi hotspot or mesh)
* Use `ROS_MASTER_URI` or DDS multicast for ROS 2

---

## 8. Networking Architectures

### 🌐 Centralized Swarm:

* One GCS → All drones
* All MAVLink traffic routed through GCS
* Easier to debug

### 🤖 Decentralized Swarm:

* Each drone has local autonomy
* P2P links for coordination
* ROS 2 + DDS or custom protocols

```text
Drone1 ↔ Drone2 ↔ Drone3
  ↑         ↑         ↑
[UWB/Wi-Fi Mesh] + Shared Map/State
```

---

## 9. Long Range Communication

| Method        | Max Range                   | Use Case              |
| ------------- | --------------------------- | --------------------- |
| **4G/5G LTE** | Unlimited (as per coverage) | BVLOS missions        |
| **LoRa**      | \~15 km                     | Low bandwidth control |
| **RF Links**  | \~40+ km                    | Telemetry/video combo |

> 🌍 LTE + VPN (Zerotier/OpenVPN) = Remote drone control from anywhere

---

## 10. Tips for Reliable Drone Comms

✅ Use separate frequencies for RC, telemetry, and video
✅ Shield and route antennas away from ESCs
✅ Test signal loss handling: geofence, RTL
✅ Log bandwidth and latency stats
✅ Use heartbeat monitoring (MAVLink `HEARTBEAT`)

---
