<h1 align="center">🎯 Task 2.1</h1>

### **Problem Statement:**

Create a simple ROS 2 application using Python in which:

1. A **publisher node** continuously publishes the message:

   ```
   "Hi, My Name is <your_name>."
   ```

   to a topic named `/greeting` at a 1 Hz frequency.

2. A **subscriber node** subscribes to the `/greeting` topic and performs the following:

   * Displays the message received.
   * Maintains and displays a running count of how many times the message has been received.

---

#### **Expected Output Example:**

```text
[INFO] [talker]: Publishing: "Hi, My Name is AMC."
[INFO] [listener]: I heard: "Hi, My Name is AMC." | Count: 1
[INFO] [listener]: I heard: "Hi, My Name is AMC." | Count: 2
...
```

---

### ✅ Requirements:

* Use ROS 2 Humble on Ubuntu 22.04
* Use Python (`rclpy`)
* Topic name must be `/greeting`
* Use `std_msgs/msg/String` message type

---

### Deliverables:

1. Publisher Script
2. Subscriber Script
3. Screen Recording of the Task

---

### Submission:
#### Deadline: Sunday EOD, 1 June 2025
#### Submission Link: [Submit Here](https://forms.gle/gCJW1vDH7tkRnWFk9)

---
