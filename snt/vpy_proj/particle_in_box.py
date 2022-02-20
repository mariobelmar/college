"""
install first::
    $ pip install vpython

Doc:
  - https://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
  - https://www.youtube.com/watch?v=Vc3vFGQ5d2Q
"""
# import sys

from vpython import sphere, color, vector, box, rate
from vpython import gcurve, graph, arange
from math import sin, cos

ball = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.cyan)
wallR = box(pos=vector(6, 0, 0),
            size=vector(0.2, 12, 12),
            color=color.green)

ball.velocity = vector(25, 5, 0)

deltat = 0.005
t = 0
ball.pos = ball.pos + ball.velocity * deltat
i = 0
while t < 2:
    rate(70)
    if i % 20 == 0:
        print(f'ball.pos: {ball.pos}, ball.velocity: {ball.velocity}')
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    ball.pos = ball.pos + ball.velocity * deltat
    if ball.pos.x < -5 and ball.velocity.x < 0:
        ball.velocity.x = 0
        ball.velocity.y = 0
        ball.velocity.z = 0
    t = t + deltat
    i = i + 1

# sys.exit()

# graph(scroll=True, fast=False, xmin=0, xmax=10)
# g = gcurve()
# for x in arange(0,30,0.1):
#     rate(100)
#     g.plot( x, sin(x) )
