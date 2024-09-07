import math
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import time

# мок тега
def tagMock() -> int:
    return rnd.randint(-100,100)

def calculateProportion(value, rangeMin, rangeMax):
    # если значение выходит за интервал
    # берём границу
    value = max(rangeMin, value)
    value = min(rangeMax, value)
    return (value - rangeMin) / (rangeMax - rangeMin)

# интервал
tagMin = -100
tagMax = 100
# поворот
rotMin = 0
rotMax = 90
# текуцщий угол поворота
curAngleDeg = 0
curAngleRad = 0
# угол поворота с прошлого цикла
prevAngleDeg = 0
prevAngleRad = 0

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
fig.canvas.draw()
fig.canvas.flush_events()
time.sleep(0.5)

def update(i):
    global prevAngleDeg
    global prevAngleRad
    global curAngleRad
    global curAngleDeg

    value = tagMock()
    prop = calculateProportion(value, tagMin, tagMax)
    curAngleDeg = round(abs(prop) * (rotMax - rotMin), 2)
    curAngleRad = round(math.radians(curAngleDeg), 4)
    dir = "counter-clock-wise" if curAngleDeg > prevAngleDeg else "clock-wise"
    print(f"Тег: {value}; Поворот от {prevAngleDeg} ({prevAngleRad}) до {curAngleDeg} ({curAngleRad}) {dir}")
    prevAngleDeg = curAngleDeg
    prevAngleRad = round(math.radians(prevAngleDeg), 4)

    r = np.arange(2)
    theta = curAngleRad * r

    line = ax.plot(theta, r)
    time.sleep(0.5)
    return line

ani = FuncAnimation(fig, update, blit=True, save_count=100)

plt.show()
