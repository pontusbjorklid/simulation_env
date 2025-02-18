import numpy as np
import matplotlib.patches as patches

class RSU:
    def __init__(self, x, y, fov_range, fov_angle, sensor_noise, size=0.2):
        """
        Initializes the Roadside Unit (RSU).
        
        Args:
        - x, y: Position of the RSU.
        - fov_range: Sensing range of the RSU.
        - fov_angle: Tuple indicating the field of view (start_angle, end_angle).
        - sensor_noise: Standard deviation of sensor measurement noise.
        """
        self.x = x
        self.y = y
        self.fov_range = fov_range
        self.fov_angle = fov_angle
        self.sensor_noise = sensor_noise
        self.size = size

    def detect(self, pedestrian):
        """
        Simulates the RSU detecting a pedestrian within its field of view.
        Adds sensor noise to the measurement.
        """
        dx = pedestrian.x - self.x
        dy = pedestrian.y - self.y
        distance = np.sqrt(dx**2 + dy**2)

        # Check if within FoV range
        if distance > self.fov_range:
            return None  # Out of range

        # Add sensor noise to the measurement
        noisy_x = pedestrian.x + np.random.normal(0, self.sensor_noise)
        noisy_y = pedestrian.y + np.random.normal(0, self.sensor_noise)

        return np.array([noisy_x, noisy_y])

    def draw(self, ax):
        """
        Draws the RSU and its field of view.
        """
        rsu_patch = patches.Circle((self.x, self.y), self.size, edgecolor='black', facecolor='green')
        ax.add_patch(rsu_patch)

        # Draw field of view
        fov_patch = patches.Wedge(center=(self.x, self.y), r=self.fov_range,
                                  theta1=self.fov_angle[0], theta2=self.fov_angle[1],
                                  edgecolor='green', facecolor='green', alpha=0.2)
        ax.add_patch(fov_patch)
