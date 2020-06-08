import pygame


# The enemy class
# This class creates enemy objects the user fights
class Enemy:
    def __init__(self):                                     # Enemy's constructor
        self.image = pygame.image.load("alien.png")         # Load the enemy's image
        self.x_pos = 370                                    # Initialize the x position to 370
        self.y_pos = 10                                     # Initialize the y position to 10
        self.x_move = 0.03                                  # Set the x movement to 0.03

    def update_enemy(self, window):                         # Method that updates the enemy's position on the screen
        if 0 < (self.x_pos + self.x_move) < 737:            # If the x position after a move is within the borders
            self.x_pos += self.x_move                       # Change the x position
        elif (self.x_pos + self.x_move) >= 737:             # If the enemy hit the right border
            self.y_pos += 1                                 # Move the enemy down the screen a bit
            self.x_move *= -1                               # Change the enemy's x direction
        elif (self.x_pos + self.x_move) <= 0:               # If the enemy hit the left border
            self.y_pos += 1                                 # Move the enemy down the screen a bit
            self.x_move *= -1                               # Change the enemy's x direction

        window.blit(self.image, (self.x_pos, self.y_pos))   # Set the enemy's position
