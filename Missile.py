import pygame
import os
from pygame import mixer


# The Missile class
# This class create missile objects that the player object shoots
class Missile:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(        # Load the missile image
            "image_assets", "missile.png"))                 #
        self.fire_sound = mixer.Sound(os.path.join(         # Load the fire sound
             "sound_assets", "shoot.wav"))                  #
        self.hit_sound = mixer.Sound(os.path.join(          # Load the hit sound
             "sound_assets", "hit.wav"))                    #
        self.ready = True                                   # A new missile is ready to be fired
        self.x_pos = -100                                   # Initialize the x position to -100 (off screen)
        self.y_pos = -100                                   # Initialize the y pos to -100 (off screen)

    def fire(self, x):                                      # A method called by Player when the space is pressed
        if self.ready:                                      # If the missile is ready
            self.fire_sound.play()                          # Play the fire sound
            self.ready = False                              # Set the missile to unready
            self.x_pos = x + 16                             # Set it's x position to the middle of the spaceship
            self.y_pos = 445                                # Set it's y position to in front of the spaceship

    def hit(self):                                          # A method called when the missile hits an alien
        self.hit_sound.play()                               # Play the hit sound
        self.ready = True                                   # Set the missile to ready
        self.x_pos = -100                                   # Take the missile off the screen
        self.y_pos = -100                                   # Take the missile off the screen

    def update_missile(self, window):                       # A method called to update the missile's pos and display
        if not self.ready:                                  # If the rocket has been fired
            self.y_pos -= 0.1                               # Move it 0.1 pixels up the screen
            if self.y_pos <= -32:                           # If the missile has left the screen
                self.ready = True                           # The missile is ready again

        window.blit(self.image, (self.x_pos, self.y_pos))   # Update position
