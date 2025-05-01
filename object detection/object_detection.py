import cv2
import numpy as np
import os

# Define file paths for YOLOv3 weights, configuration, and COCO names
weights_path = r"yolov3.weights"
config_path = r"yolov3.cfg"
names_path = r"coco.names"
# Verify the existence of required files
if not os.path.exists(weights_path):
    raise FileNotFoundError(f"YOLO weights file not found at {weights_path}")
if not os.path.exists(config_path):
    raise FileNotFoundError(f"YOLO config file not found at {config_path}")
if not os.path.exists(names_path):
    raise FileNotFoundError(f"COCO names file not found at {names_path}")

# Load YOLOv3 model using OpenCV's dnn module
try:
    net = cv2.dnn.readNet(weights_path, config_path)
except cv2.error as e:
    raise RuntimeError(f"Error loading YOLO model: {e}")

# Get the output layer names from YOLO model
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Read class names from COCO names file
try:
    with open(names_path, "r") as f:
        classes = [line.strip() for line in f.readlines()]
except FileNotFoundError as e:
    raise RuntimeError(f"Error reading COCO names file: {e}")

# Generate a unique color for each class label
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Function to detect objects in a frame
def detect_objects(frame):
    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    return frame

# Open video capture from the laptop's camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    raise RuntimeError("Error opening video capture from the laptop's camera")

# Loop to capture frames and perform object detection
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = detect_objects(frame)
    cv2.imshow("Real-Time Object Detection", frame)

    # Exit loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()