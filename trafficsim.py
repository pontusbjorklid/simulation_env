import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import time
from pedestrian import Pedestrian
from truck import Truck
from rsu import RSU
from ego_vehicle import EgoVehicle


class TrafficSimulation:
    def __init__(self, dt=0.1, total_time=10, pedestrians=None, trucks=None, rsus=None, ego_vehicle=None):
        """
        Initializes the simulation environment.
        """
        self.dt = dt
        self.num_steps = int(total_time / dt)

        self.fig, self.ax = plt.subplots(figsize=(10, 4))
        self.setup_environment()

        self.pedestrians = pedestrians if pedestrians else []
        self.trucks = trucks if trucks else []
        self.rsus = rsus if rsus else []  # Add RSUs
        self.ego_vehicle = ego_vehicle 

    def setup_environment(self):
        """
        Draws static elements like the road.
        """
        road = patches.Rectangle((0, 3), 30, 6, edgecolor='gray', facecolor='lightgray')
        self.ax.add_patch(road)

        # Draw dashed lines for lanes
        self.ax.plot([0, 30], [6, 6], linestyle='--', color='white', linewidth=2)  # Middle lane

        # Set plot limits
        self.ax.set_xlim(0, 30)
        self.ax.set_ylim(0, 12)
        self.ax.set_aspect('equal')
        self.ax.set_xlabel('X-axis (m)')
        self.ax.set_ylabel('Y-axis (m)')

    def run(self):
        """
        Runs the simulation, updating object positions and redrawing them.
        """
        plt.ion()  # Enable interactive mode
        for _ in range(self.num_steps):
            self.ax.clear()
            self.setup_environment()

            # Move and draw pedestrians
            for pedestrian in self.pedestrians:
                pedestrian.move(self.dt)
                pedestrian.draw(self.ax)

            # Move and draw trucks
            for truck in self.trucks:
                truck.move(self.dt)
                truck.draw(self.ax)

            # Move and draw ego vehicle
            if self.ego_vehicle:
                self.ego_vehicle.move(self.dt)
                self.ego_vehicle.draw(self.ax)
                for pedestrain in self.pedestrians:
                    detection = self.ego_vehicle.detect(pedestrain)
                    if detection is not None:
                        self.ax.scatter(detection[0], detection[1], color='blue', marker='x', label='Ego Vehicle Detection')
                self.ego_vehicle.draw(self.ax)
            # Detect & draw RSUs
            for rsu in self.rsus:
                for pedestrian in self.pedestrians:
                    detection = rsu.detect(pedestrian)
                    if detection is not None:
                        self.ax.scatter(detection[0], detection[1], color='green', marker='x', label='RSU Detection')
                rsu.draw(self.ax)

            plt.draw()
            plt.pause(0.1)  # Pause for visualization

        plt.ioff()
        plt.show()
