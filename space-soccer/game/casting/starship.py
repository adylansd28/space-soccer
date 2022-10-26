from doctest import IGNORE_EXCEPTION_DETAIL
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Starship(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, body_type):
        super().__init__()
        self._construct_body(body_type)


    def _construct_body(self, body_type):
        """Constructs the starship body depending on the body_type selected
        
        Args:
            body_type (int): type of body selected
        """
        if body_type == 0:
            self.set_text("/<[:||:]>\ ")
            self.set_color(constants.GREEN)
            self.set_position(Point(360,50))
        elif body_type == 1:
            self.set_text("\<[:||:]>/")
            self.set_color(constants.RED)
            self.set_position(Point(360,500))