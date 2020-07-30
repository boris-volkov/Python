'''
========================
3D surface (solid color)
========================

Demonstrates a very basic plot of a 3D surface using a solid color.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u)*2, np.sin(v)+ 1) 
y = np.outer(np.sin(u)*2, np.sin(v)+ 1)
z = np.outer(np.ones(np.size(u)), np.sin(u))

# Plot the surface
ax.plot_surface(x, y, z, color='b')

plt.show()
