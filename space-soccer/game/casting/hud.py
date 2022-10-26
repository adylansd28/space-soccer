from doctest import IGNORE_EXCEPTION_DETAIL
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class HUD(Actor):
    """
    graphic marking of the playing field.
    
    The responsibility of the HUD is to draw on the screen the limits of the field of play for the movement of the player.

    Attributes:
        super(inherited from Actor): the same attributes that the Actor Class has.
    """
    def __init__(self):
        super().__init__()
        self._construct_body()


    def _construct_body(self):
        """Build the dimensions and shape of the HUD
        """
        self.set_color(constants.WHITE)
        self.set_position(Point(190,30))
        self.set_text("_____________________________________________\n|                                                                    |\n|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|                                                                    |\n|____________________________________________|\n|                                                                    |\n_____________________________________________")