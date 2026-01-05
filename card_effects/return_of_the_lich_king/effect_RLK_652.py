"""Effect for Unending Swarm (RLK_652).

Card Text: Resurrect all friendly minions that cost (2)
or less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass