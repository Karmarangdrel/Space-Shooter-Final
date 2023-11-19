import unittest
import pygame
from Shooter import yellow_handle_movement
from Shooter import red_handle_movement


class TestYellowHandleMovement(unittest.TestCase):
   def test_yellow_handle_movement(self):
       # Set up initial conditions
       keys_pressed = [0]*1024
       yellow = pygame.Rect(100, 300, 55, 40)

       # Call the function with the initial conditions
       yellow_handle_movement(keys_pressed, yellow)

       # Check the results
       self.assertEqual(yellow.x, 100)
       self.assertEqual(yellow.y, 300)

       # Simulate pressing the 'a' key
       keys_pressed[pygame.K_a] = 1
       yellow_handle_movement(keys_pressed, yellow)

       # Check the results
       self.assertEqual(yellow.x, 95)
       self.assertEqual(yellow.y, 300)


if __name__ == '__main__':
   unittest.main()
