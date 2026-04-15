import cv2
from ultralytics import YOLO
import easyocr
from collections import Counter

# Load YOLO model
model = YOLO("Resources/license_plate_detector.pt")

# OCR reader
reader = easyocr.Reader(['en'])

# Stability buffer
text_buffer = []
last_text = ""
frame_count = 0


def clean_text(text):
    return ''.join(filter(str.isalnum, text))


def get_stable_text(text):
    global text_buffer

    if len(text) > 4:
        text_buffer.append(text)

        if len(text_buffer) > 10:
            text_buffer.pop(0)

        most_common = Counter(text_buffer).most_common(1)
        if most_common:
            return most_common[0][0]

    return ""


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    results = model(frame)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            plate = frame[y1:y2, x1:x2]

            if plate.size == 0:
                continue

            # OCR every few frames (important)
            if frame_count % 5 == 0:
                ocr_result = reader.readtext(plate)

                if ocr_result:
                    text = ocr_result[0][-2]
                    text = clean_text(text)

                    stable = get_stable_text(text)
                    if stable:
                        last_text = stable

            # Draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Show stable text
            cv2.putText(frame, last_text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Plate", plate)

    cv2.imshow("Live Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()