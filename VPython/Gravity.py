"""
Interactive Gravity Well - Click to create planets
"""
from vpython import *

# Create scene
scene = canvas(title='Gravity Well - Click to Add Balls', width=800, height=600, background=color.black)
scene.caption = "Click anywhere to add a ball!"

# Create central mass (black hole)
central_mass = sphere(pos=vector(0, 0, 0), radius=1, color=color.red, emissive=True)

# Store all balls
balls = []


# Function to handle mouse clicks
def create_ball(evt):
    pos = scene.mouse.pos
    ball = sphere(pos=pos, radius=0.3, color=color.cyan, make_trail=True)

    # Give initial velocity perpendicular to position (creates orbits)
    direction = cross(pos, vector(0, 1, 0))
    ball.velocity = 0.3 * norm(direction)

    balls.append(ball)


# Bind click event
scene.bind("click", create_ball)

# Add some initial balls
for i in range(3):
    ball = sphere(pos=vector(5 + i, 0, 0), radius=0.3, color=color.green, make_trail=True)
    ball.velocity = vector(0, 0, 0.8 + i * 0.1)
    balls.append(ball)

# Main animation loop
dt = 0.01
while True:
    rate(100)

    for ball in balls:
        # Calculate gravitational force
        r = ball.pos - central_mass.pos
        distance = mag(r)

        if distance > 0.5:  # Avoid division by zero
            # F = G * m1 * m2 / r^2 (simplified)
            force_magnitude = -50 / (distance * distance)
            force = force_magnitude * norm(r)

            # Update velocity (F = ma -> a = F/m)
            ball.velocity = ball.velocity + force * dt

            # Update position
            ball.pos = ball.pos + ball.velocity * dt