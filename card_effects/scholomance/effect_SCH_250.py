"""Effect for Wave of Apathy (SCH_250).

Card Text: Set the Attack of all enemy minions to 1 until your next turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass