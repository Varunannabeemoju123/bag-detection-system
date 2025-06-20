import cv2
from bag_detector import detect_bag
from distance_estimator import estimate_distance
from marker_reader import read_marker
from utils import draw_info, speak

print("Select input source:")
print("1. Webcam")
print("2. Use video file: bag_demo2.mp4")
choice = input("Enter 1 or 2: ")

if choice == '1':
    cap = cv2.VideoCapture(0)
elif choice == '2':
    cap = cv2.VideoCapture("bag_demo2.mp4")
else:
    print("Invalid choice. Exiting.")
    exit()

if not cap.isOpened():
    print("Failed to open video or webcam.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame or end of video.")
        break

    bags = detect_bag(frame)

    for bag in bags:
        x, y, w, h = bag['box']
        label = bag['label']

        distance = estimate_distance(w, known_width=30, focal_length=600)

        cropped = frame[y:y+h, x:x+w]
        marker_data = read_marker(cropped)

        draw_info(frame, bag['box'], distance, label)

        if marker_data:
            speak(f"{label.capitalize()} detected. Label says: {marker_data}. Distance is approximately {int(distance)} centimeters.")
        else:
            speak(f"{label.capitalize()} detected. Distance is approximately {int(distance)} centimeters.")

    cv2.putText(frame, "Press 'Q' or ESC to exit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Bag Detection", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        print("Exit requested.")
        break

cap.release()
cv2.destroyAllWindows()
