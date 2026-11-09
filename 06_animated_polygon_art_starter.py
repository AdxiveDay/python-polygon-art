"""EXERCISE: animate multiple polygons by moving existing objects.
First finish polygon_shape.py. Then change the motion, colors, sizes,
number of polygons, and frame count to create your own artwork.
"""
import turtle
import random
import math
import time
from polygon_shape import Polygon

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Student Animated Polygon Art")
screen.bgcolor("black")
screen.tracer(0)  # The entire frame is displayed with screen.update().

rng = random.Random(17)
colors = ["cyan", "springgreen", "orange", "deepskyblue", "plum", "yellow"]
shapes = []

positions_6 = [
    (-220, 180),
    (-280, 100),
    (-290, 0),
    (-220, -100),
    (-120, -100),
    (-120, 0),
    (-200, 0)
]

positions_7 = [
    (100, 180),
    (200, 180),
    (300, 180),
    (250, 80),
    (200, -20),
    (150, -120),
    (120, -180)
]

for x,y in positions_6:
    shape = Polygon(x, y, rng.randint(3, 6), rng.randint(35, 105),
                    rng.choice(colors), rng.randint(1, 6), rng.randint(0, 359))
    shape.draw()
    shapes.append((shape, x, y, rng.random() * 6.28))

for x,y in positions_7:
    shape = Polygon(x, y, rng.randint(3, 6), rng.randint(35, 105),
                    rng.choice(colors), rng.randint(1, 6), rng.randint(0, 359))
    shape.draw()
    shapes.append((shape, x, y, rng.random() * 6.28))

for frame in range(100):
    for shape, home_x, home_y, phase in shapes:
        x = home_x + 32 * math.cos(frame * 0.07 + phase)
        y = home_y + 23 * math.sin(frame * 0.07 + phase)
        shape.move_to(x, y)  # Reuse the same object and its internal turtle.
    screen.update()
    time.sleep(0.045)  # A short delay makes motion visible.

screen.mainloop()
