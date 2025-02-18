import numpy as np
import matplotlib.patches as patches


class Pedestrian:
    def __init__(self, x, y, v_x, v_y, color, size=0.25):
        """
        Initializes a pedestrian with position and velocity.
        """
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.color = color
        self.size = size
    
    def move(self, dt):
        """
        Updates the pedestrian's position based on velocity.
        """
        self.x += self.v_x * dt
        self.y += self.v_y * dt

    def draw(self, ax):
        """
        Draws the pedestrian on the given axis.
        """
        pedestrian_patch = patches.Circle((self.x, self.y), self.size, edgecolor='black', facecolor=self.color)
        ax.add_patch(pedestrian_patch)