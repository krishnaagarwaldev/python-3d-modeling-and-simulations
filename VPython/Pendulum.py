"""
Real Double Pendulum - Chaotic Physics
"""
from vpython import *
import numpy as np

# Scene setup
scene = canvas(title='Real Double Pendulum', width=800, height=600, background=color.white)

# Pendulum parameters (real physics)
L1, L2 = 4, 3  # Lengths
m1, m2 = 2, 1  # Masses
g = 9.8  # Gravity

# Initial angles and velocities
theta1, theta2 = np.pi / 2, np.pi / 2
omega1, omega2 = 0, 0

# Create pendulum parts
pivot = sphere(pos=vector(0, 0, 0), radius=0.3, color=color.red)
bob1 = sphere(pos=vector(L1 * sin(theta1), -L1 * cos(theta1), 0), radius=0.5, color=color.blue)
bob2 = sphere(pos=bob1.pos + vector(L2 * sin(theta2), -L2 * cos(theta2), 0), radius=0.4, color=color.green)

# Create rods
rod1 = cylinder(pos=pivot.pos, axis=bob1.pos - pivot.pos, radius=0.1, color=color.black)
rod2 = cylinder(pos=bob1.pos, axis=bob2.pos - bob1.pos, radius=0.1, color=color.black)

# Trails for visualization
bob2.trail = curve(color=color.green, radius=0.05)

# Real pendulum physics simulation
dt = 0.01
while True:
    rate(100)

    # Real double pendulum equations
    num1 = -g * (2 * m1 + m2) * sin(theta1)
    num2 = -m2 * g * sin(theta1 - 2 * theta2)
    num3 = -2 * sin(theta1 - theta2) * m2
    num4 = omega2 ** 2 * L2 + omega1 ** 2 * L1 * cos(theta1 - theta2)
    den = L1 * (2 * m1 + m2 - m2 * cos(2 * theta1 - 2 * theta2))
    alpha1 = (num1 + num2 + num3 * num4) / den

    num1 = 2 * sin(theta1 - theta2)
    num2 = omega1 ** 2 * L1 * (m1 + m2)
    num3 = g * (m1 + m2) * cos(theta1)
    num4 = omega2 ** 2 * L2 * m2 * cos(theta1 - theta2)
    den = L2 * (2 * m1 + m2 - m2 * cos(2 * theta1 - 2 * theta2))
    alpha2 = (num1 * (num2 + num3 + num4)) / den

    # Update angular velocities
    omega1 += alpha1 * dt
    omega2 += alpha2 * dt

    # Update angles
    theta1 += omega1 * dt
    theta2 += omega2 * dt

    # Update positions
    bob1.pos = vector(L1 * sin(theta1), -L1 * cos(theta1), 0)
    bob2.pos = bob1.pos + vector(L2 * sin(theta2), -L2 * cos(theta2), 0)

    # Update rods
    rod1.axis = bob1.pos - pivot.pos
    rod2.pos = bob1.pos
    rod2.axis = bob2.pos - bob1.pos

    # Add to trail
    bob2.trail.append(bob2.pos)