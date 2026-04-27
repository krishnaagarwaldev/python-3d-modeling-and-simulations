"""
Simple Bouncing Balls - Physics Simulation
"""
from vpython import *
import numpy as np

# Create scene
scene = canvas(title='Bouncing Balls', width=800, height=600, background=color.white)

# Create walls
wall_right = box(pos=vector(12, 0, 0), size=vector(0.2, 20, 20), color=color.blue)
wall_left = box(pos=vector(-12, 0, 0), size=vector(0.2, 20, 20), color=color.blue)
wall_top = box(pos=vector(0, 10, 0), size=vector(24, 0.2, 20), color=color.blue)
wall_bottom = box(pos=vector(0, -10, 0), size=vector(24, 0.2, 20), color=color.blue)
wall_back = box(pos=vector(0, 0, -10), size=vector(24, 20, 0.2), color=color.blue)

# Create balls with different properties
balls = []
colors = [color.red, color.green, color.yellow, color.orange, color.purple]

for i in range(5):
    ball = sphere(pos=vector(i - 2, 0, 0), radius=0.5, color=colors[i])
    ball.velocity = vector(np.random.uniform(-3, 3), np.random.uniform(-3, 3), np.random.uniform(-3, 3))
    balls.append(ball)

# Main animation loop
dt = 0.01
while True:
    rate(100)

    for ball in balls:
        # Update position
        ball.pos = ball.pos + ball.velocity * dt

        # Bounce off walls
        if ball.pos.x > 11.5 or ball.pos.x < -11.5:
            ball.velocity.x = -ball.velocity.x
        if ball.pos.y > 9.5 or ball.pos.y < -9.5:
            ball.velocity.y = -ball.velocity.y
        if ball.pos.z > 9.5 or ball.pos.z < -9.5:
            ball.velocity.z = -ball.velocity.z