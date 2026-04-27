"""
3D Maze Escape Game
"""
from vpython import *
import random

game_won = 0

# Game setup
scene = canvas(title='Maze Escape', width=1000, height=700, background=color.gray(0.3))
scene.caption = "Use WASD to move, find the green exit!"

# Player
player = sphere(pos=vector(0, 0.5, 0), radius=0.4, color=color.blue)

# Create maze walls
walls = []
maze_size = 8

# Outer walls
walls.append(box(pos=vector(0, 0, maze_size), size=vector(maze_size * 2, 2, 0.2), color=color.red))
walls.append(box(pos=vector(0, 0, -maze_size), size=vector(maze_size * 2, 2, 0.2), color=color.red))
walls.append(box(pos=vector(maze_size, 0, 0), size=vector(0.2, 2, maze_size * 2), color=color.red))
walls.append(box(pos=vector(-maze_size, 0, 0), size=vector(0.2, 2, maze_size * 2), color=color.red))

# Random inner walls
for i in range(15):
    x = random.randint(-maze_size + 1, maze_size - 1)
    z = random.randint(-maze_size + 1, maze_size - 1)
    if abs(x) > 2 or abs(z) > 2:  # Don't block start area
        walls.append(box(pos=vector(x, 0, z), size=vector(1, 2, 1), color=color.red))

# Create exit
exit = box(pos=vector(maze_size - 1, 0, 0), size=vector(0.2, 2, 1), color=color.green)

# Game state
game_won = False
win_text = label(pos=vector(0, 5, 0), text="", height=30, color=color.yellow)


# Keyboard controls
def keydown(evt):
    if game_won:
        return

    old_pos = player.pos.copy()

    if evt.key == 'w':
        player.pos.z -= 0.5
    elif evt.key == 's':
        player.pos.z += 0.5
    elif evt.key == 'a':
        player.pos.x -= 0.5
    elif evt.key == 'd':
        player.pos.x += 0.5

    # Check wall collisions
    for wall in walls:
        if mag(player.pos - wall.pos) < 1.5:
            player.pos = old_pos
            break

    # Check if reached exit
    if mag(player.pos - exit.pos) < 1.5:
        # global game_won
        game_won = True
        win_text.text = "YOU ESCAPED! YOU WIN!"


scene.bind('keydown', keydown)

# Camera follows player
while True:
    rate(60)
    scene.center = player.pos