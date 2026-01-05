"""Effect for Hedge Maze (CORE_REV_333).

Card Text: Trigger a friendly minion's <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass