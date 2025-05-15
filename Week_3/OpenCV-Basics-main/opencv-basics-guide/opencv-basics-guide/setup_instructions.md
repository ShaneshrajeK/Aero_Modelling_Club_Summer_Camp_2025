# OpenCV Setup Instructions

This guide will walk you through setting up your system for OpenCV development using Python on Windows, Linux, and MacOS. We also include optional setup for Jupyter Notebooks.

🧰 Prerequisites

Python 3.7+

pip (Python package installer)

Git (optional, for cloning repositories)

🪟 Windows Setup

1. Install Python

Download and install the latest version of Python from python.org. Ensure you check the box "Add Python to PATH" during installation.

2. Open Command Prompt and Create a Virtual Environment (optional)

python -m venv opencv-env
opencv-env\Scripts\activate

3. Install OpenCV and Dependencies

pip install opencv-python numpy matplotlib

🐧 Linux Setup (Ubuntu/Debian)

1. Update and Install Python3 and pip

sudo apt update
sudo apt install python3 python3-pip python3-venv

2. Create and Activate a Virtual Environment (optional)

python3 -m venv opencv-env
source opencv-env/bin/activate

3. Install OpenCV and Dependencies

pip install opencv-python numpy matplotlib

🍎 MacOS Setup

1. Install Homebrew (if not already installed)

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. Install Python (if needed)

brew install python

3. Create Virtual Environment and Activate (optional)

python3 -m venv opencv-env
source opencv-env/bin/activate

4. Install OpenCV and Dependencies

pip install opencv-python numpy matplotlib

📒 Optional: Jupyter Notebook Setup

1. Install Jupyter

pip install notebook

2. Launch Jupyter

jupyter notebook

You can now open .ipynb files or create new notebooks to run OpenCV code interactively.

🧪 Test Installation

You can test if OpenCV is installed properly by running:

import cv2
print(cv2.__version__)

If the version prints without error, your setup is successful!

🆘 Troubleshooting

Use pip install opencv-python-headless if you encounter GUI issues in headless environments.

For complex installations or extra modules, refer to OpenCV official installation guide.

Happy Coding! 🚀

