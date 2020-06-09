import pygame
import math
from Player import Player
from Enemy import Enemy


# The main function
def main():
    pygame.init()                                           # Initialize pygame
    window = set_up_window()                                # Set up the window that the game plays in
    game_loop(window)                                       # Call the function to enter the game loop


# The function that creates the window, sets the title,
# and sets the icon
def set_up_window():
    window = pygame.display.set_mode((800, 600))            # Create a window 800 by 600 pixels
    pygame.display.set_caption("Space Invaders")            # Give the window a title
    icon = pygame.image.load("RocketShip.png")              # Load an image of a space ship
    pygame.display.set_icon(icon)                           # Set the image as the icon in the top left of the window
    return window


# The function that deals with hit detection and determines
# if the missile hit the alien
def check_collision(enemy, player):
    enemy_x = enemy.x_pos + 20                              # Get the x pos near center of enemy (pic isn't centered)
    enemy_y = enemy.y_pos + 30                              # Get the y pos near center of enemy (pic isn't centered)
    missile_x = player.missile.x_pos                        # Get the x pos of the missile
    missile_y = player.missile.y_pos                        # Get the y pos of the missile

    distance = math.pow(enemy_x-missile_x, 2) +\
               math.pow(enemy_y-missile_y, 2)               # Calculate using the distance formula
    distance = math.sqrt(distance)                          # Calculate using the distance formula

    if distance < 35:                                       # If the distance is less than 35 pixels
        return True                                         # Return true (there was a hit)
    else:                                                   # Otherwise
        return False                                        # Return false (there was NOT a hit)


# The function that loops the game
def game_loop(window):
    player = Player()                                       # Create the player object
    enemies = []                                            # Create a list of enemies

    for num in range(2):                                    # Create 2 enemies and put them in a list
        enemy = Enemy()                                     #
        enemies.append(enemy)                               #

    running = True                                          # Initialize running to true
    while running:                                          # While running is true
        window.fill((0, 0, 0))                              # Uses RGB to set the background color

        for num in range(2):                                # For each enemy
            enemies[num].make_active(num+1)                 # Make the enemy active

        for event in pygame.event.get():                    # For each event in the pygame program
            if event.type == pygame.QUIT:                   # If the event is the exit button
                running = False                             # Set running to false

            if event.type == pygame.KEYDOWN:                # If a key has been pressed
                if event.key == pygame.K_LEFT:              # If the key was the left arrow key
                    player.left_pressed()                   # Call player's method left_pressed
                if event.key == pygame.K_RIGHT:             # If the key was the right arrow key
                    player.right_pressed()                  # Call player's method right_pressed
                if event.key == pygame.K_SPACE:             # If the key was the space bar
                    player.space_pressed()                  # Call player's method space_pressed

            if event.type == pygame.KEYUP:                  # If a key has been released
                if event.key == pygame.K_LEFT:              # If the released key was the left arrow key
                    player.left_released()                  # Call player's method left_released
                if event.key == pygame.K_RIGHT:             # If the key released was the right arrow key
                    player.right_released()                 # Call player's method right_released

        right_border = False                                # Initialize right_border to false
        left_border = False                                 # Initialize left border to false
        for enemy in enemies:                               # For each enemy in enemies
            if enemy.active:                                # If the enemy is active
                if check_collision(enemy, player):          # Check if the bullet hit an alien
                    player.missile.hit()                    # Call missile's hit method
                    enemy.hit()                             # Call enemy's hit method
                right_border, left_border = \
                    enemy.update_enemy(                     # Update the enemy's location
                        window, right_border, left_border)  #

        player.update_player(window)                        # Update the player's position
        pygame.display.update()                             # Update the screen to reflect any changes


main()
