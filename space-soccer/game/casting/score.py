from asyncio import constants
from game.casting.actor import Actor
from game.shared.point import Point
import constants


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
        _player (int): The number of player that the score belongs to.
    """
    def __init__(self, player):
        super().__init__()
        self._points = 0
        self._player = player
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points

        if self._player == 1:
            self.set_position(Point(600, 150))
            self.set_color(constants.GREEN)
            self.set_text(f"Player 1\n Goals: {self._points}")
        if self._player == 2:
            self.set_position(Point(600, 380))
            self.set_text(f"Player 2\n Goals: {self._points}")
            self.set_color(constants.RED)

    def get_score(self):
        """Returns the number of ponts the player has.
        
        Returns:
            points (int): The points to earned
        """
        return self._points