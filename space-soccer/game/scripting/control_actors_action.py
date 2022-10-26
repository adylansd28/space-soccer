import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.shot import Shot
import time

class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the starships, starball and the shots

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """

        self._keyboard_service = keyboard_service
        self._last_time_first = time.time()
        self._last_time_second = time.time()

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        self._star_ball = cast.get_first_actor("starballs")
        self._direction = Point(0,0)
        self._direction_second = Point(0,0)
        self._starships = cast.get_actors("starships")
        self._first_starship = self._starships[0]
        self._second_starship = self._starships[1]
        self._shots = cast.get_actors("shots")

        for shot in self._shots:
            if shot.get_position().get_y() <= 65 or shot.get_position().get_y() >= 485:
                cast.remove_actor("shots", shot)

        if self._star_ball.get_position().get_x() >= 550:
            y = self._star_ball.get_velocity().get_y()
            self._star_ball.set_velocity(Point(-10, y))
        
        if self._star_ball.get_position().get_x() <= 190:
            y = self._star_ball.get_velocity().get_y()
            self._star_ball.set_velocity(Point(10, y))
        


        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-10, 0)

            if self._first_starship.get_position().get_x() == 200:
                self._direction = Point(0,0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(10, 0)

            if self._first_starship.get_position().get_x() == 500:
                self._direction = Point(0,0)

        # first starship shot

        if self._keyboard_service.is_key_down('s'):
            new_time_first = time.time()
            time_difference_first = new_time_first - self._last_time_first

            if time_difference_first >= 0.25:
                first_new_shot = Shot(self._first_starship.get_position().add(Point(0,10)), 1)
                cast.add_actor("shots", first_new_shot)
                self._last_time_first = new_time_first




        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction_second = Point(-10, 0)

            if self._second_starship.get_position().get_x() == 200:
                self._direction_second = Point(0,0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction_second = Point(10, 0)

            if self._second_starship.get_position().get_x() == 500:
                self._direction_second = Point(0,0)

        # second starship shot
        if self._keyboard_service.is_key_down('k'):
            new_time_second = time.time()
            time_difference_second = new_time_second - self._last_time_second

            if time_difference_second >= 0.25:
                second_new_shot = Shot(self._second_starship.get_position().add(Point(0,-10)), 0)
                cast.add_actor("shots", second_new_shot)
                self._last_time_second = new_time_second


        
        self._first_starship.set_velocity(self._direction)
        self._second_starship.set_velocity(self._direction_second)