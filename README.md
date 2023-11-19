                       Description of SPACE SHOOTER pygame

Setting Up the Game window:
	The game window is created using ‘pygame. Display .set_mode(WIDTH, HEIGHT)
	The width and height of the game window are set to 900 pixels and 500 pixels, respectively using ‘WIDTH’ and ‘HEIGHT’ variables.
Classes:
 Bullet class:
	 The bullets are created using the ‘pygame.Rect’ constructor, and their movement and collision logic are handled within the ‘handle_bullets’ function.
Rocket class:
	A general class for both the player’s are rocket and enemy rocket.
	Both of the rockets color are of different where one is yellow and one is red.
	It manages the rockets position, health of each players, image, bullets, and shooting mechanism.
Functions:
Overall functions:
	Draws the game window, including the background, borders, space-rockets, bullets, and health bars for both the space-rockets.
	Handles the movement of the Yellow space-rockets based on the keys pressed(W, A, S and D)
	Handles the movement of the Red space-rockets based on the keys pressed(arrow keys)

 Main Game loop:
	It handles the collision, both player’s health and the game state like showing the player who won or lost.
	Inside the game loop, it checks for player input like keyboard keys.

Closing the game:
	The game will continues to run and play until one players quite the game or the one who lose to other after finishing the lives/ health of the player.
	After the game ends, a “RED WINS!” are displaying in the middle, If red wins over the yellow and it will be displayed same even for YELLOW rockets, if Yellow wins over the RED.
REASONS FOR CHOOSING THE UNIT TEST?

1. Good code quality: writing unit tests often leads to better code design and modularity. When we design code with testing in mind, we tend to create smaller, more focused functions and classes, making or code base more understandable.
2.  Early Bug Detection: Unit test allows us to catch and fix bugs early in the development process. By testing individual components of our code in isolation, we can identify and address issues before it propagate to other parts of the system.
3. Documentation: Unit tests will serves as a documentation. As it will provide the examples of using the code and by reading the tests, it allows the developers to gain insights into the expected behavior of different components.
4. Regression Testing: Unit tests act as a form of regression testing, ensuring that new changes don’t introduce unexpected side effects or break existing functionality, this becomes especially important as a project evolves and more features are added.


