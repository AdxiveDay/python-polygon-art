"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle

class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        
        if sides < 3:
            ValueError("cannot less than 3")
        if side_length < 0:
            ValueError("cannot less than 0")
        if pen_size < 0:
            ValueError("cannot less than 0")
        
        self.x = x
        self.y = y
        self.side = sides
        self.side_lenght = side_length
        self.color = color
        self.pen_size = pen_size
        self.angle = angle

        self.t1 = turtle.Turtle()

    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        # TODO: lift pen; go to starting vertex; set heading/color/pensize;
        #       lower pen; draw sides; lift pen.
        self.t1.penup()
        self.t1.goto(self.x, self.y)
        self.t1.setheading(self.angle)
        self.t1.color(self.color)
        self.t1.pensize(self.pen_size)
        self.t1.pendown()
        for _ in range(self.side):
            self.t1.forward(self.side_lenght)
            self.t1.left(360/self.side)
        self.t1.penup()

    def move_to(self, x, y):
        """Move polygon to a new position."""

        self.x = x
        self.y = y

        self._pen.clear()

        self.draw()
