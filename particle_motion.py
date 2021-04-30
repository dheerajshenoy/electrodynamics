import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

def E(r0, x, y):
    denom = np.hypot(x-r0[1], y-r0[2])**3
    return r0[0] * (x - r0[1])/denom, r0[0] * (y - r0[2])/denom

fig, ax = plt.subplots()
WIDTH, HEIGHT = 4, 4
ax.set_xlim(-WIDTH, WIDTH)
ax.set_ylim(-HEIGHT, HEIGHT)

nx, ny = 64, 64
x, y = np.linspace(-WIDTH, WIDTH, nx), np.linspace(-HEIGHT, HEIGHT, ny)
X, Y = np.meshgrid(x, y)

def animate(frame):
    Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
    ax.collections = []
    ax.patches = []
    charges = [[1e-10,1, 1], [-1e-10, -1*frame/10, 1*frame/10]]
    for charge in charges:
        ex, ey = E(charge, x=X, y=Y)
        Ex += ex
        Ey += ey
        ax.add_artist(Circle(radius=0.1, xy=(charge[1],charge[2])))
    color = 2 * np.log(np.hypot(Ex, Ey))
    ln = ax.streamplot(X, Y, Ex, Ey, density=2, arrowstyle='->', linewidth=1, arrowsize=1.5, cmap=plt.cm.inferno)
    return ln

anim = FuncAnimation(fig, animate, frames=100, interval=50, blit=False, repeat=False)
anim.save('animation.gif', writer='imagemagick')
