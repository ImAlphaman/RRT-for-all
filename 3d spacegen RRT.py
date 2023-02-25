''' copyright (c) 2022 Abhishek Thakur '''


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the boundaries of the space
x_min, x_max = -10, 10
y_min, y_max = -10, 10
z_min, z_max = -10, 10

# Create a figure and a 3D axis object
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the limits of the plot
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
ax.set_zlim([z_min, z_max])

# Generate some random obstacles in the space
num_obstacles = 20
obstacle_centers = np.random.uniform(low=[x_min, y_min, z_min], high=[x_max, y_max, z_max], size=(num_obstacles, 3))
obstacle_radii = np.random.uniform(low=0.2, high=2.5, size=num_obstacles)

# Plot the obstacles
for center, radius in zip(obstacle_centers, obstacle_radii):
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = radius * np.cos(u) * np.sin(v) + center[0]
    y = radius * np.sin(u) * np.sin(v) + center[1]
    z = radius * np.cos(v) + center[2]
    ax.plot_surface(x, y, z, color='grey', alpha=0.8)

# Define a function to check if a point is inside an obstacle
def inside_obstacle(point, obstacle_center, obstacle_radius):
    return np.linalg.norm(point - obstacle_center) <= obstacle_radius

# Define a function to generate a random point in the space
def random_point():
    return np.random.uniform(low=[x_min, y_min, z_min], high=[x_max, y_max, z_max])