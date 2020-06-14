import pygame
import os


# The enemy class
# This class creates enemy objects the user fights
class Enemy:
    def __init__(self):                                     # Enemy's constructor
        self.image = pygame.image.load(os.path.join(        # Load the enemy's image
            "image_assets", "alien.png"))                   #
        self.x_pos = 850                                    # Initialize the x position to 850
        self.y_pos = 0                                      # Initialize the y position to 0
        self.x_move = 0                                     # Initialize the x movement to 0
        self.active = False                                 # Set active flag to false
        self.dead = False                                   # Set dead flag to false
        self.speed_multiplier = 1                           # Initialize the speed multiplier to 1

    def make_active(self, num):                             # A method that makes enemies active
        if not self.active and not self.dead:               # If the enemy is not already active and not already dead
            if num == 0:                                    # If this is enemy 0
                self.active = True                          # Set active to true
                self.x_pos = 170                            # Set the x position to 170
                self.y_pos = 10                             # Set the y position to 10
                self.x_move = 0.03                          # Set the x movement to 0.03
                self.x_move *= self.speed_multiplier        # Multiply the movement by the speed multiplier
            elif num == 1:                                  # If this is enemy 1
                self.active = True                          # Set active to true
                self.x_pos = 570                            # Set the x position to 570
                self.y_pos = 10                             # Set the y position to 10
                self.x_move = 0.03                          # Set the x movement to 0.03
                self.x_move *= self.speed_multiplier        # Multiply the movement by the speed multiplier
            elif num == 2:                                  # If this is enemy 2
                self.active = True                          # Set active to true
                self.x_pos = 370                            # Set the x position to 370
                self.y_pos = 10                             # Set the y position to 10
                self.x_move = 0.03                          # Set the x movement to 0.03
                self.x_move *= self.speed_multiplier        # Multiply the movement by the speed multiplier
            elif num == 3:                                  # If this is enemy 3
                self.active = True                          # Set active to true
                self.x_pos = 170                            # Set the x position to 170
                self.y_pos = 84                             # Set the y position to 84
                self.x_move = 0.03                          # Set the x movement to 0.03
                self.x_move *= self.speed_multiplier        # Multiply the movement by the speed multiplier
            elif num == 4:                                  # If this is enemy 4
                self.active = True                          # Set active to true
                self.x_pos = 570                            # Set the x position to 570
                self.y_pos = 84                             # Set the y position to 84
                self.x_move = 0.03                          # Set the x movement to 0.03
                self.x_move *= self.speed_multiplier        # Multiply the movement by the speed multiplier
            elif num == 5:                                  # If this is enemy 5
                self.active = True                          # Set active to true
                self.x_pos = 370                            # Set the x position to 570
                self.y_pos = 84                             # Set the y position to 84
                self.x_move = 0.03                          # Set the x movement to 0.03
                self.x_move *= self.speed_multiplier        # Multiply the movement by the speed multiplier

    def hit(self):                                          # A method that is called when a missile hits the enemy
        self.x_pos = 850                                    # Move the enemy off of the screen
        self.y_pos = 0                                      # Move the enemy off of the screen
        self.x_move = 0                                     # Set the x movement to 0
        self.active = False                                 # Set the active flag to false
        self.dead = True                                    # Set the dead flag to true

    def change_direction(self):                             # A method called when the enemies' directions are changed
        self.y_pos += 30                                    # Move the enemy down the screen a bit
        self.x_move *= -1                                   # Change the enemy's x direction

    def update_enemy(self, window):                         # Method that updates the enemy's position on the screen
        if self.dead:                                       # If the enemy is dead
            window.blit(self.image,                         # Set the enemy's position
                        (self.x_pos, self.y_pos))           #
            return False                                    # Return False (no direction change)

        change_direction = False                            # Create change_direction flag and initialize to false
        if 0 < (self.x_pos + self.x_move) < 737:            # If the x position after a move is within the borders
            self.x_pos += self.x_move                       # Change the x position
        elif (self.x_pos + self.x_move) >= 737:             # If the enemy hit the right border
            change_direction = True                         # Set change_direction flag to true
        elif (self.x_pos + self.x_move) <= 0:               # If the enemy hit the left border
            change_direction = True                         # Set change direction flag to true

        window.blit(self.image, (self.x_pos, self.y_pos))   # Set the enemy's position
        return change_direction                             # Return change_direction
