import pygame

pygame.mixer.init()

try:
    click_sound = pygame.mixer.Sound("click_sound.mp3")  # Load sound
    click_sound.set_volume(1.0)  # Set max volume
    print("Sound loaded successfully! Playing now...")
    click_sound.play()
    pygame.time.delay(1000)  # Wait 1 second to let the sound play
except pygame.error as e:
    print("Pygame sound error:", e)

