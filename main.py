import pygame
from Player import Player
from Enemy import Enemy


# The main function
def main():
    pygame.init()                                           # Initialize pygame
    window = set_up_window()                                # Set up the window that the game plays in
    game_loop(window)                                       # Call the function to enter the game loop


def set_up_window():
    window = pygame.display.set_mode((800, 600))            # Create a window 800 by 600 pixels
    pygame.display.set_caption("Space Invaders")            # Give the window a title
    icon = pygame.image.load("RocketShip.png")              # Load an image of a space ship
    pygame.display.set_icon(icon)                           # Set the image as the icon in the top left of the window
    return window


def game_loop(window):
    player = Player()                                       # Create the player object
    enemy = Enemy()                                         # Create the enemy object

    running = True                                          # Initialize running to true
    while running:                                          # While running is true
        window.fill((0, 0, 0))                              # Uses RGB to set the background color

        for event in pygame.event.get():                    # For each event in the pygame program
            if event.type == pygame.QUIT:                   # If the event is the exit button
                running = False                             # Set running to false

            if event.type == pygame.KEYDOWN:                # If a key has been pressed
                if event.key == pygame.K_LEFT:              # If the key was the left arrow key
                    player.left_pressed()                   # Call player's method left_pressed
                if event.key == pygame.K_RIGHT:             # If the key was the right arrow key
                    player.right_pressed()                  # Call player's method right_pressed
                if event.key == pygame.K_UP:                # If the key was the up arrow key
                    player.up_pressed()                     # Call player's method up_pressed
                if event.key == pygame.K_DOWN:              # If the key was the down arrow key
                    player.down_pressed()                   # Call player's method down_pressed

            if event.type == pygame.KEYUP:                  # If a key has been released
                if event.key == pygame.K_LEFT:              # If the released key was the left arrow key
                    player.left_released()                  # Call player's method left_released
                if event.key == pygame.K_RIGHT:             # If the key released was the right arrow key
                    player.right_released()                 # Call player's method right_released
                if event.key == pygame.K_UP:                # If the key released was the up arrow key
                    player.up_released()                    # Call the player's method up_released
                if event.key == pygame.K_DOWN:              # If the key released was the down arrow key
                    player.down_released()                  # Call the player's method down_released

        player.update_player(window)                        # Update the player's position
        enemy.update_enemy(window)                          # Update the enemy's position
        pygame.display.update()                             # Update the screen to reflect any changes


main()
