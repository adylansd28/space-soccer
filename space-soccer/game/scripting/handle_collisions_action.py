import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a Shot collides
    with the other Shot, with the limits of the field or with the Starballs

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        self._timer = cast.get_first_actor("timer")

        if self._timer.get_time() == 0:
            self._is_game_over = True

        if not self._is_game_over:
            self._handle_starball_shot_collision(cast)
            self._handle_shot_shot_collision(cast)
            self._handle_goal_collision(cast)
        else:
            self._handle_game_over(cast)
    
    def _handle_starball_shot_collision(self, cast):
        """Handles how the starball reacts to shot collision
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        self._starball = cast.get_first_actor("starballs")

        self._shots = cast.get_actors("shots")

        area = []

        for row in range(-20,21):
            for col in range(-20,21):
                area.append(Point(row, col))

        counter = 0
        for i in area:
            area[counter] = self._starball.get_position().add(i)
            counter +=1

        for shot in self._shots:
            for _i in area:
                if shot.get_position().equals(_i):
                    if shot.get_direction() == 0:
                        x = self._starball.get_velocity().get_x()
                        self._starball.set_velocity(Point(x,-10))
                    elif shot.get_direction() == 1:
                        x = self._starball.get_velocity().get_x()
                        self._starball.set_velocity(Point(x,10))

    def _handle_shot_shot_collision(self, cast):
        """Handles how a Shot reacts to other shot collision.
        """
        self._shots = cast.get_actors("shots")

        for shot in self._shots:
            for _shot in self._shots:
                if shot != _shot:
                    if shot.get_position().equals(_shot.get_position()):
                        cast.remove_actor("shots", shot)
                        cast.remove_actor("shots", _shot)
                        return

    def _handle_goal_collision(self, cast):
        """Handles how the starball and scores reacts to starball collision with goal
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        self._starball = cast.get_first_actor("starballs")
        self._scores = cast.get_actors("scores")

        if  self._starball.get_position().get_y() <= 65:
            self._starball.construct_body()
            self._scores[1].add_points(1)


        if self._starball.get_position().get_y() >= 485:
            self._starball.construct_body()
            self._scores[0].add_points(1)
            
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the starships white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        self._starships = cast.get_actors("starships")

        for starship in self._starships:
            starship.set_color(constants.WHITE)
        
        self._starball = cast.get_first_actor("starballs")
        self._scores = cast.get_actors("scores")

        self._starball.set_text("")

        game_over = cast.get_first_actor("game_over")
        game_over.set_position(Point(330, 280))

        if self._scores[0].get_score() > self._scores[1].get_score():
            game_over.set_text("Player 1 has WON!")
        elif self._scores[0].get_score() < self._scores[1].get_score():
            game_over.set_text("Player 2 has WON!")
        elif self._scores[0].get_score() == self._scores[1].get_score():
            game_over.set_text("This is a DRAW!")

        