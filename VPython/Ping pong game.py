"""
3D Pong Game
"""
from vpython import *

# Game setup
scene = canvas(title='3D Pong', width=1000, height=700, background=color.black)
scene.caption = "Player 1: A/D | Player 2: Left/Right Arrow"

# Create paddles and ball
paddle1 = box(pos=vector(-9,0,0), size=vector(0.5,3,1), color=color.blue)
paddle2 = box(pos=vector(9,0,0), size=vector(0.5,3,1), color=color.red)
ball = sphere(pos=vector(0,0,0), radius=0.5, color=color.white, make_trail=True)

# Game variables
ball.velocity = vector(4, 3, 0)
scores = [0, 0]

# Score display
score_display = label(pos=vector(0,8,0), text=f'{scores[0]} - {scores[1]}',
                     height=30, color=color.white)

# Keyboard controls
def keydown(evt):
    if evt.key == 'a' and paddle1.pos.y < 5:
        paddle1.pos.y += 1
    elif evt.key == 'd' and paddle1.pos.y > -5:
        paddle1.pos.y -= 1
    elif evt.key == 'left' and paddle2.pos.y < 5:
        paddle2.pos.y += 1
    elif evt.key == 'right' and paddle2.pos.y > -5:
        paddle2.pos.y -= 1

scene.bind('keydown', keydown)

# Main game loop
while True:
    rate(60)

    # Move ball
    ball.pos = ball.pos + ball.velocity * 0.05

    # Ball collision with top/bottom walls
    if ball.pos.y > 6 or ball.pos.y < -6:
        ball.velocity.y = -ball.velocity.y

    # Ball collision with paddles
    if (ball.pos.x < paddle1.pos.x + 0.8 and abs(ball.pos.y - paddle1.pos.y) < 1.5):
        ball.velocity.x = -ball.velocity.x * 1.1  # Speed up
        ball.velocity.y += (ball.pos.y - paddle1.pos.y) * 0.5  # Add spin

    if (ball.pos.x > paddle2.pos.x - 0.8 and abs(ball.pos.y - paddle2.pos.y) < 1.5):
        ball.velocity.x = -ball.velocity.x * 1.1  # Speed up
        ball.velocity.y += (ball.pos.y - paddle2.pos.y) * 0.5  # Add spin

    # Score points
    if ball.pos.x < -10:
        scores[1] += 1
        ball.pos = vector(0,0,0)
        ball.velocity = vector(4, 3, 0)
    elif ball.pos.x > 10:
        scores[0] += 1
        ball.pos = vector(0,0,0)
        ball.velocity = vector(-4, 3, 0)

    # Update score display
    score_display.text = f'{scores[0]} - {scores[1]}'