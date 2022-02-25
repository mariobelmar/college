"""

"""

from vpython import sphere, color, vector, box, rate
from vpython import gcurve, graph, arange
from math import sin, cos

ball = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.blue)

wallrx = box(pos=vector(6, 0, 0),
            size=vector(0.2, 12, 12),
            color=color.red)
walllx = box(pos=vector(-6, 0, 0),
            size=vector(0.2, 12, 12),
        color=color.red)
wallby = box(pos=vector(0, 6, 0),
            size=vector(12, 0.2, 12),
            color=color.red)
walluy = box(pos=vector(0, -6, 0),
            size=vector(12, 0.2, 12),
            color=color.red)


ball.velocity = vector(5, 100, 0)

deltat = 0.005
t = 0
ball.pos = ball.pos + ball.velocity * deltat
i = 0
while True:  # :t < 2.5:
    rate(100)
    if i % 20 == 0:
        print(f'ball.pos: {ball.pos}, ball.velocity: {ball.velocity}')
    if ball.pos.x > wallrx.pos.x:
        ball.velocity.x = -ball.velocity.x
    ball.pos = ball.pos + ball.velocity * deltat

    t = t + deltat
    i = i + 1

    if ball.pos.x < walllx.pos.x:
        ball.velocity.x = -ball.velocity.x
    ball.pos = ball.pos + ball.velocity * deltat

    if ball.pos.y > walluy.pos.y:
        ball.velocity.y = -ball.velocity.y
    ball.pos = ball.pos + ball.velocity * deltat

    if ball.pos.y < wallby.pos.y:
        ball.velocity.y = -ball.velocity.y


