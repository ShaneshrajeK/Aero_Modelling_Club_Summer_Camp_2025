
# 🧠 OpenCV Basics — Learn Computer Vision with Python

Welcome to the **OpenCV Basics** repository! This project is designed to teach fundamental concepts of Computer Vision using Python and the OpenCV library. Whether you're a beginner or someone brushing up on CV concepts, this structured and practical guide will help you understand the key principles step-by-step.

---

## 📂 Repository Structure

```bash
OpenCV-Basics/
├── 01_Introduction_to_OpenCV/
│   ├── intro.md                   # Explains what OpenCV is and how it works
│   └── basic_operations.py        # Reading, displaying, writing images, drawing lines/shapes
│
├── 02_Image_Manipulation/
│   ├── image_read_display.py      # Loading and showing images using OpenCV
│   ├── draw_shapes.py             # Drawing lines, rectangles, circles on images
│   └── image_resize_crop.py       # Resizing and cropping operations
│
├── 03_Thresholding/
│   ├── simple_threshold.py        # Binary thresholding with fixed value
│   ├── adaptive_threshold.py      # Adaptive thresholding based on neighborhood
│   └── thresholding_comparison.md # Comparison table and explanations (merged into Setup_Instructions.md)
│
├── 04_Video_Processing/
│   ├── webcam_read.py             # Capturing video from webcam
│   └── video_record.py            # Recording and saving webcam video to a file
│
├── 05_Color_Spaces/
│   ├── hsv_conversion.py          # Convert BGR to HSV and display components
│   └── masking_colors.py          # Apply color masks (e.g. detect red, blue)
│
├── 06_Image_Thresholding/
│   └── thresholding.md            # Overview of thresholding with examples
│
├── Setup_Instructions.md          # Cross-platform OpenCV setup instructions with notebook support
├── requirements.txt               # Python dependencies (opencv-python, numpy, matplotlib)

```

---

## 📌 What You Will Learn

| Module | Topics Covered                                   |
| ------ | ------------------------------------------------ |
| `01`   | Introduction to OpenCV, Reading & writing images |
| `02`   | Drawing shapes, Resizing, Cropping, Flipping     |
| `03`   | Simple vs Adaptive Thresholding                  |
| `04`   | Real-time video capture & video writing          |
| `05`   | BGR to HSV conversion, Color masking             |
| `06`   | Thresholding Theory and Use-Cases                |
| Setup  | Installation on Windows/Linux/MacOS              |
| Bonus  | Jupyter Notebook support                         |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Shubham9653830781/OpenCV-Basics.git
cd OpenCV-Basics
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Run any example

```bash
python 01_Introduction_to_OpenCV/basic_operations.py
```

---

## 🛠️ Requirements

The project requires the following Python packages:

```
opencv-python
numpy
matplotlib
```

You can install them via:

```bash
pip install -r requirements.txt
```

---

## 🧰 Setup Instructions

We support setup on **Windows**, **Linux**, and **Mac**. See the full guide here:
📄 [Setup\_Instructions.md](./opencv-basics-guide/opencv-basics-guide/setup_instructions.md)

---

## 🧭 Learning Flow:
1. Image Basics → 
2. Color Spaces → 
3. Thresholding → 
4. Contours & Shapes → 
5. Real-Time Video Tasks →
6. Deep Learning with OpenCV (future)


## 📚 Recommended Learning Path

To build toward advanced CV tasks like object detection, shape segmentation, and pose estimation, follow this roadmap:

1. **OpenCV Basics** (this repo)
2. **Contours and Morphology**
3. **Feature Matching (ORB/SIFT)**
4. **Human Detection (YOLO, SSD)**
5. **Pose Detection with MediaPipe**
6. **VSLAM & Visual Tracking (ORB-SLAM)**


---
