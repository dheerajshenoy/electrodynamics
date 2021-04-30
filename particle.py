import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

charges = []
S = sys.argv[1:]
for i in S:
    q = i.split(',')
    q = [float(i) for i in q]
    print(q)
    charges.append(q)

def E(r0, x, y):
    denom = np.hypot(x-r0[1], y-r0[2])**3
    return r0[0] * (x - r0[1])/denom, r0[0] * (y - r0[2])/denom

fig, ax = plt.subplots()

WIDTH, HEIGHT = 4, 4
ax.set_xlim(-WIDTH, WIDTH)
ax.set_ylim(-HEIGHT, HEIGHT)

nx, ny = 64, 64
x = np.linspace(-WIDTH, WIDTH, nx)
y = np.linspace(-HEIGHT, HEIGHT, ny)
X, Y = np.meshgrid(x, y)
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))

if(len(charges) == 0): exit(0)

for charge in charges:
    ex, ey = E(charge, x=X, y=Y)
    Ex += ex
    Ey += ey
    ax.add_artist(Circle(radius=0.1, xy=(charge[1],charge[2])))

color = 2 * np.log(np.hypot(Ex, Ey))
ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, arrowstyle='simple, head_width=0.2', arrowsize=1.5, density=2, cmap=plt.cm.cividis)
plt.show()
