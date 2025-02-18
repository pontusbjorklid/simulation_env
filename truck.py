import numpy as np
import matplotlib.patches as patches

class Truck:
    def __init__(self, x, y, v_x, v_y, color, length=6, width= 2.5):
        """
        Initializes a truck with position and velocity.
        """
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.color = color
        self.length = length
        self.width = width
    
    def move(self, dt):
        """
        Updates the truck's position based on velocity.
        """
        self.x += self.v_x * dt
        self.y += self.v_y * dt
    
    def draw(self, ax):
        """
        Draws the truck on the given axis.
        """
        truck_patch = patches.Rectangle((self.x, self.y), self.length, self.width, edgecolor='black', facecolor=self.color)
        ax.add_patch(truck_patch)
