import cv2
import pytesseract

# Set the path for Windows Tesseract install
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_marker(image):
    qr_decoder = cv2.QRCodeDetector()
    data, _, _ = qr_decoder.detectAndDecode(image)
    if data:
        return data

    text = pytesseract.image_to_string(image)
    return text.strip()
