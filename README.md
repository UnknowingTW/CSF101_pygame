# CSF101_pygame
Here's a simple description of what this code does:

    It imports necessary libraries, including random, pygame, and sys.
    It defines some constants like the game window's size, cell size, colors, and directions.
    It sets up the game window, initializes fonts, and displays the start screen with a rotating title.
    The runGame function handles the main game loop. It allows the player to control a "worm" using arrow keys or WASD keys to collect apples.
    The worm grows longer when it consumes an apple, and the game ends if the worm collides with the game boundaries or itself.
    The showGameOverScreen function displays a "Game Over" message when the game ends.
    The terminate function quits the game when necessary.
    The drawGrid, drawWorm, drawApple, and drawScore functions are responsible for drawing the game elements on the screen.
    The game logic is mainly within the runGame function, where the worm's movements, collisions, and apple consumption are handled.
    The main game loop runs continuously until the player decides to quit or the game ends.
