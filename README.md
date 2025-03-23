#Create code for projects in future
This is the codespace for what i have in mind for my future research project


📌 How Code Works (Overview)
Your eye-tracking cursor with blink click system works in these steps:
Captures video from your webcam.
Detects your face and eyes using Dlib's face landmark predictor.
Finds your eye positions and calculates an average position.
Maps that position to a 3x3 grid (to determine cursor movement).
Moves the mouse cursor based on where you're looking.
Detects blinks using the Eye Aspect Ratio (EAR).
Plays a click sound and triggers a mouse click when a blink is detected.



1️⃣ Project Title & Description
📌 Eye-Tracking Cursor with Blink Click
This project allows users to control their mouse cursor using eye movements and perform a click action by blinking. It uses OpenCV, Dlib, PyAutoGUI, and Pygame for implementation.

2️⃣ Features
✅ Moves the cursor based on eye position
✅ Clicks when you blink
✅ Plays a click sound when blinking
✅ Uses a 3x3 grid system for smoother tracking


## Installation  
1. Clone this repository:  
git clone https://github.com/FariaSamanta/SHANA.git cd SHANA

markdown
Copy
Edit

2. Install dependencies:  
pip install -r requirements.txt

markdown
Copy
Edit

3. Extract the shape predictor model:  
python extract_bz2.py

shell
Copy
Edit

## Usage  
Run the main script:  
python eye_tracking_cursor.py

markdown
Copy
Edit

📌 Run the code:

bash
Copy
Edit
python eye_tracking_cursor.py
4️⃣ How to Use
1️⃣ Run the script and look at different areas of the screen.
2️⃣ Your cursor will follow your eye movements.
3️⃣ Blink to trigger a mouse click.
4️⃣ Press Q to exit.

5️⃣ Known Issues & Future Improvements
⚠ May need calibration for different lighting conditions.
⚠ Cursor movement can be refined for smoother control.
✨ Future improvement: Implement a larger grid system for more precise tracking.


## Dependencies  
- `OpenCV`  
- `dlib`  
- `numpy`  
- `pygame` (for sound)  

## Files in This Repository
- `eye_tracking_cursor.py` – Main program  
- `shape_predictor_68_face_landmarks.dat.bz2` – Model for face tracking (must be extracted)  
- `click_sound.mp3` – Click sound effect  
- `test_sound.py` – For testing the sound  

## Contributors  
- **Faria Samanta Akbar** 🎉  

## License  
This project is open-source. Feel free to modify and improve it!  

