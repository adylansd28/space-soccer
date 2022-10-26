from game.scripting.action import Action
from game.shared.point import Point


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        scores = cast.get_actors("scores")
        starships = cast.get_actors("starships")
        starball = cast.get_first_actor("starballs")
        hud = cast.get_first_actor("HUD")
        shots = cast.get_actors("shots")
        timer = cast.get_first_actor("timer")
        game_over = cast.get_first_actor("game_over")

        timer.set_time(1)

        self._video_service.clear_buffer()
        self._video_service.draw_actor(hud)
        self._video_service.draw_actors(starships)
        self._video_service.draw_actors(shots)
        self._video_service.draw_actor(starball)
        self._video_service.draw_actors(scores)
        self._video_service.draw_actor(timer)
        self._video_service.draw_actor(game_over)
        self._video_service.flush_buffer()