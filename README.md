# Real-Time Object Detection Using YOLOv3 and OpenCV

This project implements real-time object detection using the powerful YOLOv3 (You Only Look Once) algorithm with OpenCV in Python. YOLOv3 is known for its speed and accuracy, making it one of the most popular algorithms for object detection tasks.

---

![Image](https://github.com/user-attachments/assets/ccdc5d30-1e6a-4416-a92d-e74ab9357912)

---
### 🔗 Download YOLOv3 Weights
[Download yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)  
Place it in the project root folder.

---



## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)


---

## Features
- Real-time object detection using YOLOv3.
- Utilizes OpenCV for video processing.
- Pre-trained weights for detecting objects in images and videos.
- Easily configurable for custom datasets and models.

---



## Installation

Follow these steps to set up the project:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RAHUL04012006/object_detection.git
   cd object_detection
   ```

2. **Install dependencies:**
   Ensure you have Python installed. Then, install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLOv3 weights:**
   Download the pre-trained weights for YOLOv3 from the [official YOLO website](https://pjreddie.com/darknet/yolo/). Place the weights file in the project's directory.

4. **Setup configuration files:**
   Ensure the `yolov3.cfg` and `coco.names` files are in the directory along with the weights.

---

## Usage

1. **Run the object detection script:**
   ```bash
   python object_detection.py --input <input_file> --output <output_file>
   ```
   Replace `<input_file>` with the path to your input video or image and `<output_file>` with the desired output path.

2. **Real-time detection with webcam:**
   To use your webcam for real-time object detection, simply run:
   ```bash
   python object_detection.py --webcam
   ```

3. **Custom models:**
   - Replace the `yolov3.cfg`, `yolov3.weights`, and `coco.names` files with your custom-trained files if you wish to detect objects from a custom dataset.

---

## Results
Here are some example output from the model:

![Image](https://github.com/user-attachments/assets/ccdc5d30-1e6a-4416-a92d-e74ab9357912)

  
---

## Contributing

Contributions are welcome! If you'd like to improve this project, follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

