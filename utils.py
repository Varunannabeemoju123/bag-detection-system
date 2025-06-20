import cv2
import pyttsx3
import queue
import threading

tts = pyttsx3.init()
tts.setProperty('rate', 150)

speech_queue = queue.Queue()

def speech_worker():
    while True:
        text = speech_queue.get()
        if text is None:
            break
        try:
            tts.say(text)
            tts.runAndWait()
        except RuntimeError:
            print("Speech error occurred.")
        speech_queue.task_done()

# Start the speech thread once
threading.Thread(target=speech_worker, daemon=True).start()

def speak(text):
    if speech_queue.qsize() < 5:
        speech_queue.put(text)

def draw_info(frame, box, distance, label=None):
    x, y, w, h = box
    color = (0, 255, 0)
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    info = f"{label.capitalize()}, Distance: {int(distance)} cm" if label else f"Distance: {int(distance)} cm"
    cv2.putText(frame, info, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
