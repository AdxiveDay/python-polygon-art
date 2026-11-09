"""EXERCISE: make overlapping polygon art like the reference image.
Complete polygon_shape.py first. Then adjust the parameters below to
create your own composition. The example uses a black background.
"""
import turtle
import random
from polygon_shape import Polygon

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Student Polygon Art")
screen.bgcolor("black")
screen.tracer(0)  # We draw the whole scene before refreshing the screen.

colors = ["cyan", "turquoise", "orange", "yellowgreen", "deepskyblue",
          "salmon", "plum", "lightgreen", "gold", "pink", "white"]
rng = random.Random(12)

polygons = []

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

for x, y in positions_6:
    sides = rng.randint(3,6)
    side_length = 50
    color = colors[2]
    pen_size = rng.randint(1, 7)
    angle = 0

    polygon = Polygon(
        x, y, sides, side_length,
        color, pen_size, angle
    )

    polygon.draw()
    polygons.append(polygon)
    
for x, y in positions_7:
    sides = rng.randint(3,6)
    side_length = 50
    color = colors[5]
    pen_size = rng.randint(1, 7)
    angle = 0

    polygon = Polygon(
        x, y, sides, side_length,
        color, pen_size, angle
    )

    polygon.draw()
    polygons.append(polygon)

screen.update()
screen.mainloop()
