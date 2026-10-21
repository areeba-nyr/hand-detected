
import cv2
import mediapipe as mp
import sys

print("=== FROST MIRROR DIAGNOSTIC ===")
print("Python:", sys.version)
print("OpenCV:", cv2.__version__)
print("MediaPipe:", mp.__version__)

if not hasattr(mp, "solutions"):
    print("ERROR: MediaPipe hand tracking API is unavailable.")
    print("Check which MediaPipe installation your virtual environment uses.")
    raise SystemExit(1)

print("Hand tracking API: OK")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Could not open camera 0.")
    camera.release()
    raise SystemExit(1)

print("Camera: OK")
print("Press Q or ESC to close the test window.")

try:
    with mp.solutions.hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    ) as hands:

        while True:
            success, frame = camera.read()

            if not success:
                print("ERROR: Camera frame could not be read.")
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if result.multi_hand_landmarks:
                hand = result.multi_hand_landmarks[0]
                h, w = frame.shape[:2]

                fingertip = hand.landmark[8]
                x = int(fingertip.x * w)
                y = int(fingertip.y * h)

                cv2.circle(frame, (x, y), 15, (0, 255, 0), -1)
                cv2.putText(
                    frame, "HAND DETECTED",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 2
                )
                cv2.putText(
                    frame, f"Finger: {x}, {y}",
                    (20, 75), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 255, 255), 2
                )
                mp.solutions.drawing_utils.draw_landmarks(
                    frame, hand, mp.solutions.hands.HAND_CONNECTIONS
                )
            else:
                cv2.putText(
                    frame, "SHOW YOUR HAND",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 0, 255), 2
                )

            cv2.imshow("Frost Mirror - Camera Test", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == 27:
                break

finally:
    camera.release()
    cv2.destroyAllWindows()
    print("Diagnostic test closed.")


