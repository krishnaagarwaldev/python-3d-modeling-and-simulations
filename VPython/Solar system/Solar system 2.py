"""
Real Solar System with Actual Data
"""
from vpython import *
import numpy as np

# Scene setup
scene = canvas(title='Real Solar System', width=1000, height=700, background=color.black)

# Real planetary data (scaled)
sun = sphere(pos=vector(0,0,0), radius=10, color=color.yellow, emissive=True)

# Planets: [name, distance(AU), radius, color, orbital period(years)]
planets_data = [
    ["Earth", 15, 2, color.blue, 1],
    ["Mars", 23, 1.5, color.red, 1.88],
    ["Jupiter", 40, 5, color.orange, 11.86]
]

planets = []
for data in planets_data:
    planet = sphere(pos=vector(data[1], 0, 0), radius=data[2], color=data[3], make_trail=True)
    planet.angle = 0
    planet.period = data[4]
    planets.append(planet)

# Add stars background
for i in range(500):
    star = sphere(pos=vector(np.random.uniform(-200,200),
                          np.random.uniform(-200,200),
                          np.random.uniform(-200,200)),
                 radius=np.random.uniform(0.1,0.3),
                 color=color.white, opacity=0.7)

# Real orbital motion
while True:
    rate(60)
    for planet in planets:
        planet.angle += (2 * np.pi) / (planet.period * 365) * 5  # Speed factor
        planet.pos.x = planets_data[planets.index(planet)][1] * cos(planet.angle)
        planet.pos.z = planets_data[planets.index(planet)][1] * sin(planet.angle)