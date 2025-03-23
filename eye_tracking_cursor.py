import cv2
import dlib
import pyautogui
import numpy as np
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()
click_sound = pygame.mixer.Sound("click_sound.mp3")

# Initialize Dlib's face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Start webcam capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow to avoid MSMF errors

def calculate_ear(eye_points, landmarks):
    """Calculate the Eye Aspect Ratio (EAR) to detect blinking."""
    A = np.linalg.norm(np.array((landmarks.part(eye_points[1]).x, landmarks.part(eye_points[1]).y)) - 
                        np.array((landmarks.part(eye_points[5]).x, landmarks.part(eye_points[5]).y)))
    B = np.linalg.norm(np.array((landmarks.part(eye_points[2]).x, landmarks.part(eye_points[2]).y)) - 
                        np.array((landmarks.part(eye_points[4]).x, landmarks.part(eye_points[4]).y)))
    C = np.linalg.norm(np.array((landmarks.part(eye_points[0]).x, landmarks.part(eye_points[0]).y)) - 
                        np.array((landmarks.part(eye_points[3]).x, landmarks.part(eye_points[3]).y)))
    return (A + B) / (2.0 * C)

# Blink detection parameters
EAR_THRESHOLD = 0.2
BLINK_FRAMES = 3
blink_counter = 0
open_counter = 0
blink_detected = False

def run_eye_tracking():
    global blink_counter, open_counter, blink_detected
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        
        for face in faces:
            # Draw a rectangle around the face
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 255), 2)

            landmarks = predictor(gray, face)
            
            # Eye landmark points
            left_eye_pts = [36, 37, 38, 39, 40, 41]
            right_eye_pts = [42, 43, 44, 45, 46, 47]
            
            left_ear = calculate_ear(left_eye_pts, landmarks)
            right_ear = calculate_ear(right_eye_pts, landmarks)
            avg_ear = (left_ear + right_ear) / 2.0
            
            # Get eye region points
            left_eye = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in left_eye_pts])
            right_eye = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in right_eye_pts])

            # Draw eye bounding boxes
            cv2.polylines(frame, [left_eye], True, (0, 255, 0), 1)  # Green
            cv2.polylines(frame, [right_eye], True, (0, 255, 0), 1)  # Green

            # ✅ Draw a blue dot on the pupil (approximation)
            left_pupil = (int((landmarks.part(36).x + landmarks.part(39).x) / 2), int((landmarks.part(37).y + landmarks.part(41).y) / 2))
            right_pupil = (int((landmarks.part(42).x + landmarks.part(45).x) / 2), int((landmarks.part(43).y + landmarks.part(47).y) / 2))
            
            cv2.circle(frame, left_pupil, 3, (255, 0, 0), -1)  # Blue dot on pupil
            cv2.circle(frame, right_pupil, 3, (255, 0, 0), -1)  # Blue dot on pupil
            
            # ✅ Blink detection logic
            if avg_ear < EAR_THRESHOLD:
                blink_counter += 1
                open_counter = 0  # Reset open counter
                
                if blink_counter >= BLINK_FRAMES and not blink_detected:
                    print("Blink detected!")
                    pygame.mixer.Sound.play(click_sound)
                    pyautogui.click()
                    blink_detected = True
            else:
                open_counter += 1
                if open_counter > 5:  # Ensure eyes stay open before resetting blink detection
                    blink_counter = 0
                    blink_detected = False

        cv2.imshow("Eye Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the main function
if __name__ == "__main__":
    run_eye_tracking()



