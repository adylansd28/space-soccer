from doctest import IGNORE_EXCEPTION_DETAIL
import constants
from game.casting.actor import Actor
from game.shared.point import Point
import time


class Timer(Actor):
    """
    countdown timer
    
    The timer's responsibility is to count down to 0 and cause the game to end.

    Attributes:
        _time (int): the countdown in seconds
        _sys_time(float): system referential timestamp
    """
    def __init__(self):
        super().__init__()
        self._time = 45
        self._sys_time = time.time()
        self._construct_body()

    def _construct_body(self):
        """Constructs the timer graphic
        """
        self.set_text(f"Time Left: {self._time}")
        self.set_color(constants.WHITE)
        self.set_position(Point(600, 280))

    def set_time(self, add_time):
        """updates the amount of time remaining to finish the
        
        Args:
            add_time (int): how many seconds are removed from the timer in each iteration of the program
        """
        new_sys_time = time.time()
        time_difference = new_sys_time - self._sys_time
        if int(time_difference) == 1:
            if self._time > 0:
                self._time -= add_time
                self._sys_time = new_sys_time
        self.set_text(f"Time Left: {self._time} seconds")

    def get_time(self):
        return self._time