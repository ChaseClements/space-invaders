import pygame


# The player class
# This class creates the spaceship object that the user plays as
class Player:
    def __init__(self):                                     # The constructor
        self.image = pygame.image.load("spaceship.png")     # Load the player's image
        self.x_pos = 370                                    # Initialize the x position to 370
        self.y_pos = 480                                    # Initialize the y position to 480
        self.x_move = 0                                     # Initialize the x movement to 0
        self.y_move = 0                                     # Initialize the y movement to 0
        self.left_pushed = False                            # Initialize var indicating if left key is pushed to false
        self.right_pushed = False                           # Initialize var indicating if right key is pushed to false
        self.up_pushed = False                              # Initialize var indicating if up key is pushed to false
        self.down_pushed = False                            # Initialize var indicating if down key is pushed to false

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

    def up_pressed(self):                                   # A method that is called when the up key is pressed
        self.y_move = -0.2                                  # Set y movement to 0.2 pixels up the screen
        self.up_pushed = True                               # Set up_pushed boolean var to true

    def up_released(self):                                  # A method that is called when the up key is released
        self.up_pushed = False                              # Set up_pushed boolean var to false
        if self.down_pushed:                                # If the down arrow key is pressed
            self.y_move = 0.2                               # Set y movement to 0.2 pixels down the screen
        else:                                               # Else (the down arrow key is not pressed)
            self.y_move = 0                                 # Set y movement to 0

    def down_pressed(self):                                 # A method that is called when the down key is pressed
        self.y_move = 0.2                                   # Set y movement to 0.2 pixels down the screen
        self.down_pushed = True                             # Set down_pushed boolean var to true

    def down_released(self):                                # A method that is called when the down key is released
        self.down_pushed = False                            # Set down_pushed boolean var to false
        if self.up_pushed:                                  # If the up arrow key is pressed
            self.y_move = -0.2                              # Set y movement to 0.2 pixels up the screen
        else:                                               # Else (the up arrow key is not pressed)
            self.y_move = 0                                 # Set y movement to 0

    def update_player(self, window):                        # Method that updates the player's position on screen
        if 0 < (self.x_pos + self.x_move) < 737:            # If the x position after a move is within the borders
            self.x_pos += self.x_move                       # Change the x position
        if 2 < (self.y_pos + self.y_move) < 535:            # If the y position after a move is within the borders
            self.y_pos += self.y_move                       # Change the y position

        window.blit(self.image, (self.x_pos, self.y_pos))   # Update position
