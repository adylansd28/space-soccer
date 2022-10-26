from doctest import IGNORE_EXCEPTION_DETAIL
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Shot(Actor):
    """
    A shot of Starship ammunition.
    
    The responsibility of a Shot is to move until it collides with another shot, the end of the playing field or the Starball.

    Attributes:
        _diection_type (int): determines whether to move up or down.
    """
    def __init__(self, init_pos, direction_type):
        super().__init__()
        self.set_position(init_pos)
        self.set_color(constants.GREEN)
        self._construct_body()
        self._direction_type = direction_type
        self._set_direction_type(direction_type)

    def _construct_body(self):
        """Constructs the body of the Shot
        """
        self.set_text("©")

    def _set_direction_type(self, dir_type):
        """Set the direction the shot will have in game
        
        Args:
            dir_type (int): Move up or move down
        """
        if dir_type == 0:
            self.set_velocity(Point(0,-10))
            self.set_color(constants.RED)
        elif dir_type == 1:
            self.set_velocity(Point(0,10))
            self.set_color(constants.GREEN)

    def get_direction(self):
        """Returns the directions the Shot has
        
        Args:
            points (int): Type of direction the Shot has.
        """
        return self._direction_type