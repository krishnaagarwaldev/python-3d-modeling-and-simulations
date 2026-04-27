"""
Real Physics Bouncing with Gravity and Energy Loss
"""
from vpython import *
import numpy as np

# Scene setup
scene = canvas(title='Real Physics Bouncing', width=800, height=600, background=color.white)

# Create floor
floor = box(pos=vector(0, -5, 0), size=vector(20, 0.2, 10), color=color.green)

# Real physics parameters
gravity = vector(0, -9.8, 0)  # Real gravity
energy_loss = 0.8  # 20% energy loss on bounce

# Create balls with different masses
balls = []
for i in range(3):
    ball = sphere(pos=vector(i * 3 - 3, 0, 0), radius=0.5,
                  color=vector(np.random.random(), np.random.random(), np.random.random()))
    ball.velocity = vector(0, 10, 0)  # Initial upward velocity
    ball.mass = 1.0
    balls.append(ball)

# Real physics simulation
dt = 0.01
while True:
    rate(100)

    for ball in balls:
        # Apply gravity (F = ma -> a = F/m)
        acceleration = gravity
        ball.velocity = ball.velocity + acceleration * dt

        # Update position
        ball.pos = ball.pos + ball.velocity * dt

        # Realistic bounce with energy loss
        if ball.pos.y - ball.radius <= floor.pos.y + floor.size.y / 2:
            ball.pos.y = floor.pos.y + floor.size.y / 2 + ball.radius
            ball.velocity.y = -ball.velocity.y * energy_loss  # Energy loss on bounce

            # Stop if velocity is very small
            if abs(ball.velocity.y) < 0.5:
                ball.velocity.y = 0