# bag-detection-system
# 🧳 Real-Time Conveyor Belt Luggage Detection and Distance Estimation

This project is a real-time, AI-powered assistive system that helps visually impaired individuals detect and locate their luggage on conveyor belts in public spaces like airports and metro stations. It performs object detection, distance estimation, and audio feedback — all offline and optimized for both desktop and edge computing platforms.

---

## 🚀 Key Features

- 🎒 Detects luggage types: backpacks, suitcases, handbags, carriers
- 📏 Estimates distance from the user using the pinhole camera model
- 🔍 Reads printed labels using OCR (Tesseract) or QR codes
- 🗣️ Provides offline speech feedback (e.g., "Suitcase detected. Distance 85 centimeters")
- 🎥 Supports both webcam and video input
- ⚡ Lightweight, runs smoothly on Jetson Nano or low-end PCs

---

## 🧠 How It Works

- **YOLOv8n** is used for real-time object detection
- **OpenCV** handles frame capture, resizing, and drawing
- **Tesseract** or **pyzbar** reads bag labels
- **pyttsx3** gives voice feedback (thread-safe version)
- Works offline without cloud dependencies

---

## 🧰 Technologies Used

- Python 3.11+
- YOLOv8 (Ultralytics)
- OpenCV
- pyttsx3 or espeak
- Tesseract OCR
- NumPy

---

## 📁 Project Structure

bag_detector_project/
├── main.py # Main logic loop (webcam/video, detection, audio)
├── bag_detector.py # YOLOv8 detection function
├── distance_estimator.py # Distance estimation logic
├── marker_reader.py # OCR / QR detection
├── utils.py # Drawing + speech queue
├── yolov8n.pt # YOLOv8 model weights
├── bag_demo2.mp4 # Sample input video
├── requirements.txt # Install packages


---

## ▶ Getting Started

1. **Install dependencies:**

```bash
pip install -r requirements.txt

2.Install Tesseract OCR:

Windows: https://github.com/tesseract-ocr/tesseract
3.Run the project:

bash
Copy
Edit
python main.py

4.Choose:

css
Copy
Edit
1 → Webcam input
2 → Video file (e.g., bag_demo2.mp4)

5.Press Q to quit.

##**DISTANCE ESTIMATION**
Uses the formula:

ini
Copy
Edit
Distance = (Known Width × Focal Length) / Detected Width

Where:

>Known Width = physical width of luggage in cm

>Detected Width = bounding box width in pixels

>Focal Length = calibrated based on a reference frame

**ACKNOWLEDGEMENTS**
>Ultralytics YOLOv8

>OpenCV

>Tesseract OCR

##📌 Future Enhancements
*Add wearable version (smart glasses)

*Enable vibration feedback for hearing-impaired users

*ONNX export + TensorRT for speed boost

*Mobile app integration via Bluetooth or Wi-Fi

*Multi-object audio management and alert delay

