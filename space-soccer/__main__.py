import constants
import random

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.starship import Starship
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.casting.hud import HUD
from game.casting.timer import Timer
from game.casting.actor import Actor
from game.casting.starball import Starball


def main():

    first_player = Starship(0)
    second_player = Starship(1)
    star_ball = Starball()
    hud = HUD()
    first_score = Score(1)
    second_score = Score(2)
    timer = Timer()
    game_over = Actor()
    game_over.set_text("")
    game_over.set_position(Point(900, 600))


    # create the cast
    cast = Cast()
    cast.add_actor("starships", first_player)
    cast.add_actor("starships", second_player)
    cast.add_actor("starballs", star_ball)
    cast.add_actor("HUD", hud)
    cast.add_actor("scores", first_score)
    cast.add_actor("scores", second_score)
    cast.add_actor("timer", timer)
    cast.add_actor("game_over", game_over)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()