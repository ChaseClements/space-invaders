import pygame


# The enemy class
# This class creates enemy objects the user fights
class Enemy:
    def __init__(self):                                     # Enemy's constructor
        self.image = pygame.image.load("alien.png")         # Load the enemy's image
        self.x_pos = 850                                    # Initialize the x position to 850
        self.y_pos = 0                                      # Initialize the y position to 0
        self.x_move = 0                                     # Initialize the x movement to 0
        self.active = False                                 # Set active flag to false
        self.dead = False                                   # Set dead flag to false

    def make_active(self, num):                             # A method that makes enemies active
        if not self.active and not self.dead:               # If the enemy is not already active and not already dead
            if num == 1:                                    # If this is enemy 1
                self.active = True                          # Set active to true
                self.x_pos = 170                            # Set the x position to 170
                self.y_pos = 10                             # Set the y position to 10
                self.x_move = 0.03                          # Set the x movement to 0.03
            elif num == 2:                                  # If this is enemy 2
                self.active = True                          # Set active to true
                self.x_pos = 570                            # Set the x position to 570
                self.y_pos = 10                             # Set the y position to 10
                self.x_move = 0.03                          # Set the x movement to 0.03

    def hit(self):                                          # A method that is called when a missile hits the enemy
        self.x_pos = 850                                    # Move the enemy off of the screen
        self.y_pos = 0                                      # Move the enemy off of the screen
        self.x_move = 0                                     # Set the x movement to 0
        self.active = False                                 # Set the active flag to false
        self.dead = True                                    # Set the dead flag to true

    def update_enemy(self, window, r_border, l_border):     # Method that updates the enemy's position on the screen
        if 0 < (self.x_pos + self.x_move) < 737:            # If the x position after a move is within the borders
            self.x_pos += self.x_move                       # Change the x position
        elif (self.x_pos + self.x_move) >= 737 or r_border: # If the enemy hit the right border or another enemy did
            r_border = True                                 # Set r_border to true
            self.y_pos += 10                                # Move the enemy down the screen a bit
            self.x_move *= -1                               # Change the enemy's x direction
        elif (self.x_pos + self.x_move) <= 0 or l_border:   # If the enemy hit the left border or another enemy did
            l_border = True                                 # Set l_border to true
            self.y_pos += 10                                # Move the enemy down the screen a bit
            self.x_move *= -1                               # Change the enemy's x direction

        window.blit(self.image, (self.x_pos, self.y_pos))   # Set the enemy's position
        return r_border, l_border                           # Return whether the right or left borders have been hit
