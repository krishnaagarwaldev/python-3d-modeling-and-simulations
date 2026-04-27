"""
Solar System Simulation using VPython
A 3D simulation of our solar system with planets orbiting the Sun
"""

from vpython import *
import numpy as np

# Set up the scene
scene = canvas(title='Solar System Simulation', width=1200, height=800,
               background=color.black, center=vector(0, 0, 0))

# Disable autoscaling
scene.autoscale = False

# Create stars in the background
stars = []
for i in range(500):
    x = np.random.uniform(-1000, 1000)
    y = np.random.uniform(-1000, 1000)
    z = np.random.uniform(-1000, 1000)
    star = sphere(pos=vector(x, y, z), radius=np.random.uniform(0.1, 0.5),
                  color=color.white, opacity=0.7)


# Celestial body class
class CelestialBody:
    def __init__(self, name, radius, color, distance, orbital_period, tilt=0):
        self.name = name
        self.radius = radius
        self.color = color
        self.distance = distance
        self.orbital_period = orbital_period
        self.angle = 0
        self.tilt = tilt

        # Create the sphere
        self.sphere = sphere(pos=vector(distance, 0, 0), radius=radius,
                             color=color, make_trail=True, trail_type='points',
                             trail_radius=0.1, interval=10, retain=500)

        # Add label
        self.label = label(pos=self.sphere.pos, text=name, height=10,
                           box=False, opacity=0, color=color)

    def update_position(self, time):
        # Calculate orbital position
        self.angle = (time / self.orbital_period) * 2 * np.pi
        x = self.distance * np.cos(self.angle)
        z = self.distance * np.sin(self.angle) * np.cos(np.radians(self.tilt))
        y = self.distance * np.sin(self.angle) * np.sin(np.radians(self.tilt))

        self.sphere.pos = vector(x, y, z)
        self.label.pos = self.sphere.pos


# Create the Sun
sun = sphere(pos=vector(0, 0, 0), radius=20, color=color.yellow,
             emissive=True, texture=textures.rough)

# Create planets (scaled for better visualization)
# Parameters: name, radius, color, distance, orbital_period (Earth days), axial_tilt
planets = [
    CelestialBody("Mercury", 3, color.gray(0.7), 40, 88, 0.1),
    CelestialBody("Venus", 5, color.orange, 60, 225, 177.4),
    CelestialBody("Earth", 5.5, color.blue, 80, 365, 23.5),
    CelestialBody("Mars", 4, color.red, 100, 687, 25.2),
    CelestialBody("Jupiter", 12, color.orange, 140, 4333, 3.1),
    CelestialBody("Saturn", 10, color.yellow, 180, 10759, 26.7),
    CelestialBody("Uranus", 8, color.cyan, 220, 30687, 97.8),
    CelestialBody("Neptune", 8, color.blue, 260, 60190, 28.3)
]

# Create Saturn's rings
saturn_rings = ring(pos=planets[5].sphere.pos, axis=vector(0, 1, 0),
                    radius1=15, radius2=22, thickness=0.5, color=color.yellow)

# Information display
info_text = label(pos=vector(-150, 100, 0),
                  text="Solar System Simulation\n\nControls:\n• Mouse: Rotate view\n• Scroll: Zoom\n• Click planets for info",
                  height=14, box=False, color=color.white)

# Time control variables
time_speed = 1
paused = False
current_time = 0


# Create control buttons and sliders
def toggle_pause():
    global paused
    paused = not paused


def set_speed(s):
    global time_speed
    time_speed = s.value


# Control panel
scene.append_to_caption("\n\nControls:\n")

pause_button = button(bind=toggle_pause, text="Pause/Resume")
scene.append_to_caption("  ")

speed_slider = slider(min=0, max=10, value=1, length=300, bind=set_speed)
scene.append_to_caption(" Simulation Speed\n")


# Click handler for planet information
def get_planet_info(evt):
    picked = scene.mouse.pick
    if picked and hasattr(picked, 'name'):
        for planet in planets:
            if planet.sphere == picked:
                info_text.text = f"Planet: {planet.name}\n"
                info_text.text += f"Distance from Sun: {planet.distance} units\n"
                info_text.text += f"Orbital Period: {planet.orbital_period} days\n"
                info_text.text += f"Radius: {planet.radius} units"
                break


scene.bind("click", get_planet_info)

# Main simulation loop
dt = 1  # Time step (days per frame)

while True:
    rate(30)  # Maximum 30 frames per second

    if not paused:
        current_time += dt * time_speed

        # Update planet positions
        for planet in planets:
            planet.update_position(current_time)

        # Update Saturn's rings position
        saturn_rings.pos = planets[5].sphere.pos

        # Update information text
        info_text.text = f"Solar System Simulation\n\n"
        info_text.text += f"Simulation Time: {current_time:.0f} days\n"
        info_text.text += f"Time Speed: {time_speed}x\n"
        info_text.text += f"Status: {'Paused' if paused else 'Running'}\n\n"
        info_text.text += "Click on any planet for more info"