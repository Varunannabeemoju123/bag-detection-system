from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Detect these object classes
TARGET_CLASSES = ['backpack', 'handbag', 'suitcase']

def detect_bag(frame):
    results = model(frame)[0]
    detections = []

    for box in results.boxes:
        class_id = int(box.cls)
        class_name = model.names[class_id]

        if class_name in TARGET_CLASSES:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append({
                'box': (x1, y1, x2 - x1, y2 - y1),
                'label': class_name
            })

    return detections
