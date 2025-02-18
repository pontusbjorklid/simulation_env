from trafficsim import TrafficSimulation
from pedestrian import Pedestrian
from truck import Truck
from rsu import RSU
from ego_vehicle import EgoVehicle


# Create objects
ego_vehicle = EgoVehicle(x=0, y=3.25, v_x=0, v_y=0, color='blue', fov_range=10, fov_angle=(-30, 30), sensor_noise=0.5)
pedestrians = [Pedestrian(x=18, y=0.5, v_x=-0.5, v_y=0.5, color='red')]
trucks = [Truck(x=10, y=0.5, v_x=0, v_y=0, color='black')]
rsus = [RSU(x=18, y=10, fov_range=10, fov_angle=(-150, -30), sensor_noise=0.5)]

# Run the simulation with objects
sim = TrafficSimulation(dt=0.1, total_time=10, pedestrians=pedestrians, trucks=trucks, rsus=rsus, ego_vehicle=ego_vehicle)
sim.run()
