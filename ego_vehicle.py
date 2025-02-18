import numpy as np
import matplotlib.patches as patches

class EgoVehicle:
    def __init__(self, x, y, v_x, v_y, color, fov_range, fov_angle, sensor_noise, length=6, width=2.5):
        """
        Initializes the ego vehicle with position, velocity, and dimensions.

        Args:
        - x, y: Initial position.
        - v_x, v_y: Velocity in x and y directions.
        - length, width: Vehicle dimensions.
        - color: Vehicle color for visualization.
        """
        # Position
        self.x = x
        self.y = y
        # Velocity
        self.v_x = v_x
        self.v_y = v_y
        # Sensor
        self.fov_range = fov_range
        self.fov_angle = fov_angle
        self.sensor_noise = sensor_noise
        # Cosmetics
        self.length = length
        self.width = width
        self.color = color

    def detect(self, pedestrian):
        """
        Simulates the ego vehicle detecting a pedestrian within its field of view.
        """
        dx = pedestrian.x - self.x
        dy = pedestrian.y - self.y
        distance = np.sqrt(dx**2 + dy**2)

        # Check if within sensing range
        if distance > self.fov_range:
            return None
        # Add sensor noise to the measurement
        noisy_x = pedestrian.x + np.random.normal(0, self.sensor_noise)
        noisy_y = pedestrian.y + np.random.normal(0, self.sensor_noise)
        
        return np.array([noisy_x, noisy_y])

    def move(self, dt):
        """
        Updates the ego vehicle's position based on velocity.
        """
        self.x += self.v_x * dt
        self.y += self.v_y * dt

    def draw(self, ax):
        """
        Draws the ego vehicle on the given axis.
        """
        vehicle_patch = patches.Rectangle((self.x, self.y), self.length, self.width, edgecolor='black', facecolor=self.color)
        ax.add_patch(vehicle_patch)

        # Drew field of view
        fov_patch = patches.Wedge(center=((self.x + self.length), (self.y+(self.width/2))), r=self.fov_range,
                                  theta1=self.fov_angle[0], theta2=self.fov_angle[1],
                                  edgecolor='blue', facecolor='blue', alpha=0.2)
        ax.add_patch(fov_patch)
