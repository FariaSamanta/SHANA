import cv2
import dlib
import pyautogui
import numpy as np
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()
click_sound = pygame.mixer.Sound("click_sound.mp3")  # Ensure this file exists in the same directory

# Debug: Test if sound loads
print("Sound file loaded:", pygame.mixer.get_init() is not None)

# TEST: Play sound once before main loop
pygame.mixer.Sound.play(click_sound)
input("Did you hear the sound? Press Enter to continue...")

# Initialize Dlib's face detector (HOG-based) and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Function to get the center of an eye
def get_eye_position(landmarks, eye_points):
    eye_x = np.mean([landmarks.part(point).x for point in eye_points])
    eye_y = np.mean([landmarks.part(point).y for point in eye_points])
    return int(eye_x), int(eye_y)

# Function to calculate Eye Aspect Ratio (EAR)
def calculate_ear(eye_points, landmarks):
    A = np.linalg.norm(np.array((landmarks.part(eye_points[1]).x, landmarks.part(eye_points[1]).y)) - 
                        np.array((landmarks.part(eye_points[5]).x, landmarks.part(eye_points[5]).y)))
    B = np.linalg.norm(np.array((landmarks.part(eye_points[2]).x, landmarks.part(eye_points[2]).y)) - 
                        np.array((landmarks.part(eye_points[4]).x, landmarks.part(eye_points[4]).y)))
    C = np.linalg.norm(np.array((landmarks.part(eye_points[0]).x, landmarks.part(eye_points[0]).y)) - 
                        np.array((landmarks.part(eye_points[3]).x, landmarks.part(eye_points[3]).y)))
    ear = (A + B) / (2.0 * C)
    return ear

# Blink detection parameters
EAR_THRESHOLD = 0.2  # Threshold for detecting a blink
BLINK_FRAMES = 3  # Number of consecutive frames to confirm a blink
blink_counter = 0
blink_detected = False  # To prevent repeated detections in the same blink sequence

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        
        # Blink detection
        left_ear = calculate_ear([36, 37, 38, 39, 40, 41], landmarks)
        right_ear = calculate_ear([42, 43, 44, 45, 46, 47], landmarks)
        avg_ear = (left_ear + right_ear) / 2.0
        
        if avg_ear < EAR_THRESHOLD:
            blink_counter += 1
            if blink_counter >= BLINK_FRAMES and not blink_detected:
                print("Blink detected!")  # Debug message
                pygame.mixer.Sound.play(click_sound)  # Force play sound
                pyautogui.click()  # Click event
                blink_detected = True  # Prevent repeated clicks in one blink
        else:
            blink_counter = 0
            blink_detected = False  # Reset detection for next blink
    
    cv2.imshow("Eye Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

