from vpython import *

# Create ground and a moving ball
floor = box(pos=vector(0,-0.5,0), size=vector(10,0.1,10), color=color.green)
ball = sphere(pos=vector(-4,1,0), radius=0.3, color=color.red, make_trail=True)

# Set velocity
v = vector(1,0,0)

# Animate the ball
while True:
    rate(100)              # Controls animation speed (100 frames/sec)
    ball.pos += v * 0.05   # Update position
    if ball.pos.x > 4:
        v = -v             # Bounce back
    if ball.pos.x < -4:
        v = -v
