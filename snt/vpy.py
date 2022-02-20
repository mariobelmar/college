"""
install first::
    $ pip install vpython

Doc:
  - https://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
  - https://www.youtube.com/watch?v=Vc3vFGQ5d2Q
"""
from vpython import sphere, color, vector, box, rate

# import sys

from vpython import sphere, color, vector, box, rate
from vpython import gcurve, graph, arange, rate
from math import sin, cos

"""
ball = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.cyan)
wallR = box(pos=vector(6, 0, 0), size=vector(0.2, 12, 12),
            color=color.green)
ball.velocity = vector(25, 0, 0)
deltat = 0.005
t = 0
ball.pos = ball.pos + ball.velocity * deltat

while t < 3:
    rate(100)
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    ball.pos = ball.pos + ball.velocity * deltat
    t = t + deltat

# sys.exit()

graph(scroll=True, fast=False, xmin=0, xmax=10)
g = gcurve()
for x in arange(0,30,0.1):
    rate(100)
    g.plot( x, sin(x) )
"""


grosse_boule = sphere(pos = vector(-5, -5, 0), radius=5, color=color.white)
moyenne_boule = sphere(pos = vector(-15, 0, 0), radius=3, color=color.white)
tete = sphere(pos = vector(-5, 5, 0), radius=2, color=color.white)
nez = sphere(pos = vector(0, 15, -1), radius=0.5, color=color.red)

grosse_boule.velocity = vector(5, 0, 0)
moyenne_boule.velocity = vector(-5, 0, 0)
tete.velocity = vector(5, 0, 0)

s="""
deltat = 0.005
t = 0
while t < 1 and moyenne_boule.pos.x =! grosse_boule.pos.x and
moyenne_boule.pos.x =! tete.pos.x:
    rate(100)
"""





