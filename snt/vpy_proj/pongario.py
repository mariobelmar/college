"""

"""

from vpython import sphere, color, vector, box, rate
from vpython import gcurve, graph, arange
from math import sin, cos

ball = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.blue)

wallr = box(pos=vector(6, 0, 0),
            size=vector(0.2, 12, 12),
            color=color.red)
walll = box(pos=vector(-6, 0, 0),
            size=vector(0.2, 12, 12),
        color=color.red)
wallb = box(pos=vector(0, 6, 0),
            size=vector(12, 0.2, 12),
            color=color.red)
wallu = box(pos=vector(0, -6, 0),
            size=vector(12, 0.2, 12),
            color=color.red)


ball.velocity = vector(25, 25, 0)

deltat = 0.005
t = 0
ball.pos = ball.pos + ball.velocity * deltat
i = 0
while t < 0.5:
    rate(70)
    if i % 20 == 0:
        print(f'ball.pos: {ball.pos}, ball.velocity: {ball.velocity}')
    if ball.pos.x > wallr.pos.x:
        ball.velocity.x = -ball.velocity.x
    ball.pos = ball.pos + ball.velocity * deltat
    if ball.pos.x < -5 and ball.velocity.x < 0:
        ball.velocity.x = 0
    t = t + deltat
    i = i + 1


