import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound
click_sound = pygame.mixer.Sound("click_sound.mp3")  # Make sure this file is in the same directory

# Play the sound
click_sound.play()
print("Sound is playing!")

# Keep the script running to hear the sound
input("Press Enter to exit...")
