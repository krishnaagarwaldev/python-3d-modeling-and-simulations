from vpython import *

# Parameters
mass = 0.2
k = 1        # spring constant
x0 = 1       # initial displacement
v = 0        # velocity
dt = 0.01

# Objects
wall = box(pos=vector(-1,0,0), size=vector(0.2,0.2,0.2), color=color.blue)
block = box(pos=vector(x0,0,0), size=vector(0.2,0.2,0.2), color=color.red)
spring = helix(pos=wall.pos, axis=block.pos - wall.pos, radius=0.1, coils=15, color=color.orange)

# Motion loop
while True:
    rate(100)
    F = -k * (block.pos.x - x0)    # Hooke’s Law
    a = F / mass
    v += a * dt
    block.pos.x += v * dt
    spring.axis = block.pos - wall.pos
