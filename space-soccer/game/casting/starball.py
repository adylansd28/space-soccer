from doctest import IGNORE_EXCEPTION_DETAIL
import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point


class Starball(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self.construct_body()

    def construct_body(self):
        """Constructs the body of the Starball and determines its initial direction
        """

        self.set_text("(¤)")
        self.set_position(Point(300, 280))
        self.set_color(constants.WHITE)

        left_right = random.randint(0,1)

        if left_right == 0:
            self.set_velocity(Point(-10,0))
        elif left_right == 1:
            self.set_velocity(Point(10,0))