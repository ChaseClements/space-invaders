import pygame
import math
import os
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
    icon = pygame.image.load(os.path.join(                  # Load an image of a space ship
        "image_assets", "spaceship_mini.png"))              #
    pygame.display.set_icon(icon)                           # Set the image as the icon in the top left of the window
    return window                                           # Return the window that was created


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


# The function that displays a game over message
def end_game(window, font, current_round):
    window.fill((0, 0, 0))                                  # Uses RGB to set the background color to black
    game_over = font.render("GAME OVER!", True,             # Display a game over message to the user
                            (255, 255, 255))                #
    highest_round = font.render("You got to round "         # Display the round that the player got to
                                + str(current_round),       #
                                True, (255, 255, 255))      #
    window.blit(game_over, (300, 250))                      # Print the game over message
    window.blit(highest_round, (265, 350))                  # Print the highest_round message


# The function that loops the game
def game_loop(window):
    player = Player()                                       # Create the player object
    enemies = []                                            # Create a list of enemies
    current_round = 1                                       # Initialize the current round to 1
    font = pygame.font.Font("freesansbold.ttf", 32)         #

    for num in range(6):                                    # Create 6 enemies and put them in a list
        enemy = Enemy()                                     #
        enemies.append(enemy)                               #

    running = True                                          # Initialize running to true
    while running:                                          # While running is true

        window.fill((0, 0, 0))                              # Uses RGB to set the background color

        for num in range(min(current_round, 6)):            # For each enemy
            enemies[num].make_active(num)                   # Make the enemy active

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

        round_over = True                                   # Initialize round_over to true
        for enemy in enemies:                               # For each enemy in enemies
            if enemy.active:                                # If the enemy is active
                round_over = False                          # Set round_over to false
                if check_collision(enemy, player):          # Check if the bullet hit an alien
                    player.missile.hit()                    # Call missile's hit method
                    enemy.hit()                             # Call enemy's hit method
                change_dir = enemy.update_enemy(window)     # Update the enemy's location
                if change_dir:                              # If an enemy changed it's direction
                    for obj in enemies:                     # Change all enemies' directions
                        if obj.active:                      #
                            obj.change_direction()          #
                if enemy.y_pos > 420:                       # If the enemy has reached the player
                    end_game(window, font, current_round)   # Display a game over message

        if round_over:                                      # If all the enemies are dead
            current_round += 1                              # Increment current_round
            for num in range(min(current_round, 6)):        # Make all enemies respawn
                if current_round > 6:                       # If the current round is above 6
                    enemies[num].speed_multiplier *= 1.3    # Increase the speed multiplier by 30%
                enemies[num].active = False                 #
                enemies[num].dead = False                   #

        display_round = font.render("Round: " +             # Create a variable to show the current round on screen
                                    str(current_round),     #
                                    True, (255, 255, 255))  #

        player.update_player(window)                        # Update the player's position
        window.blit(display_round, (25, 550))               # Update the current round
        pygame.display.update()                             # Update the screen to reflect any changes


main()
