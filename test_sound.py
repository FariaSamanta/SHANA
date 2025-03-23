import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound
click_sound = pygame.mixer.Sound("click_sound.mp3")  # Ensure this file exists

# Play the sound
click_sound.play()
print("Sound is playing!")


