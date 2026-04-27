"""
Simple Solar System - 3 Planets
"""
from vpython import *

# Create scene
scene = canvas(title='Simple Solar System', width=800, height=600, background=color.black)

# Create Sun
sun = sphere(pos=vector(0, 0, 0), radius=2, color=color.yellow, emissive=True)

# Create planets
planets = []
planets.append(sphere(pos=vector(5, 0, 0), radius=0.4, color=color.blue, make_trail=True))
planets.append(sphere(pos=vector(8, 0, 0), radius=0.6, color=color.red, make_trail=True))
planets.append(sphere(pos=vector(12, 0, 0), radius=0.5, color=color.green, make_trail=True))

# Planet speeds (angular velocity)
speeds = [0.02, 0.01, 0.005]
angles = [0, 0, 0]

# Main animation loop
while True:
    rate(50)

    for i in range(3):
        angles[i] += speeds[i]

        # Calculate circular orbit positions
        if i == 0:  # Mercury - close orbit
            planets[i].pos = vector(5 * cos(angles[i]), 0, 5 * sin(angles[i]))
        elif i == 1:  # Venus
            planets[i].pos = vector(8 * cos(angles[i]), 0, 8 * sin(angles[i]))
        else:  # Earth
            planets[i].pos = vector(12 * cos(angles[i]), 0, 12 * sin(angles[i]))