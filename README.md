# Real-Time Object Detection using YOLOv8

A simple **real-time object detection system** built with Python that uses a webcam to detect objects and display their labels with bounding boxes.

This project demonstrates how to integrate a deep learning object detection model with a live camera feed to perform real-time inference.

The system captures frames from a webcam, processes them through YOLOv8, and displays detected objects on the screen using OpenCV and Ultralytics.
This is a learning project built while practicing object detection with OpenCV and Python.
Some concepts were learned from documentation and online examples.
---

## Project Pipeline

Webcam → Frame Capture → YOLOv8 Model → Object Detection → Bounding Box + Label → Display

---

## Features

* Real-time object detection using webcam
* Bounding boxes around detected objects
* Object labels displayed on the screen
* Modular project structure
* Lightweight YOLOv8 Nano model for faster inference
* Easy to extend for future improvements

---

## Project Structure

object_detector-project

camera.py        → Handles webcam access
detector.py      → Loads YOLO model and performs detection
main.py          → Main application logic
yolov8n.pt       → Pretrained YOLOv8 model
requirements.txt → Project dependencies
README.md

---

## How It Works

### Camera Module

`camera.py` opens the webcam and captures frames.

### Detection Module

`detector.py` loads the YOLOv8 model and performs object detection on each frame.

### Main Application

`main.py` connects the camera and detector modules to create a complete real-time detection pipeline.

---

## Installation

Clone the repository

git clone https://github.com/VINAY-MANDAL/object_detector-project.git
cd object_detector-project

Create a virtual environment (optional)

python -m venv venv

Install dependencies

pip install -r requirements.txt

---

## Run the Project

python main.py

Press **Q** to exit the webcam window.

---

## Requirements

Python 3.10+
OpenCV
Ultralytics
YOLOv8 pretrained weights

Install manually if needed:

pip install ultralytics opencv-python

---

## Future Improvements

* FPS counter for performance monitoring
* Voice alert for detected objects
* Object counting system
* Detect only specific objects
* GUI interface using Tkinter
* Web deployment

---

## Learning Purpose

This project was built as a **learning project** to understand:

* Computer Vision basics
* Real-time object detection
* Working with YOLO models
* Integrating deep learning models with Python applications
* Structuring a modular Python project

Future updates and improvements will be added as learning progresses.

---

## Author

Vinay Mandal

GitHub:
https://github.com/VINAY-MANDAL
