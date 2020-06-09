import pygame
from Missile import Missile


# The player class
# This class creates the spaceship object that the user plays as
class Player:
    def __init__(self):                                     # The constructor
        self.image = pygame.image.load("spaceship.png")     # Load the player's image
        self.missile = Missile()                            # Create a missile object
        self.x_pos = 370                                    # Initialize the x position to 370
        self.y_pos = 480                                    # Initialize the y position to 480
        self.x_move = 0                                     # Initialize the x movement to 0
        self.left_pushed = False                            # Initialize var indicating if left key is pushed to false
        self.right_pushed = False                           # Initialize var indicating if right key is pushed to false

    def left_pressed(self):                                 # A Method that is called when left key is pressed
        self.x_move = -0.2                                  # Set x movement to 0.2 pixels to the left
        self.left_pushed = True                             # Set left_pushed boolean var to true

    def left_released(self):                                # A method that is called when left key is released
        self.left_pushed = False                            # Set left_pushed boolean var to false
        if self.right_pushed:                               # If the right arrow key is pressed
            self.x_move = 0.2                               # Set x movement to 0.2 pixels to the right
        else:                                               # Else (the right arrow key is not pressed)
            self.x_move = 0                                 # Set x movement to 0 pixels

    def right_pressed(self):                                # A method that is called when the right key is pressed
        self.x_move = 0.2                                   # Set x movement to 0.2 pixels to the right
        self.right_pushed = True                            # Set right_pushed boolean var to true

    def right_released(self):                               # A method that is called when the right key is released
        self.right_pushed = False                           # Set right_pushed boolean var to false
        if self.left_pushed:                                # If the left arrow key is pressed
            self.x_move = -0.2                              # Set x movement to 0.2 pixels to the left
        else:                                               # Else (the left arrow key is not pressed)
            self.x_move = 0                                 # Set the x movement to 0

    def space_pressed(self):                                # A method that is called when the space bar is pressed
        self.missile.fire(self.x_pos)                       # Call missile's fire method

    def get_missile_pos(self):                              # A method that is called to get the missile's position
        return self.missile.x_pos, self.missile.y_pos       # Returns the x and y positions

    def update_player(self, window):                        # Method that updates the player's position on screen
        if 0 < (self.x_pos + self.x_move) < 737:            # If the x position after a move is within the borders
            self.x_pos += self.x_move                       # Change the x position

        window.blit(self.image, (self.x_pos, self.y_pos))   # Update player's position
        self.missile.update_missile(window)                 # Update the missile's position
