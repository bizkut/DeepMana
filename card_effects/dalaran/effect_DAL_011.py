"""Effect for Lazul's Scheme (DAL_011).

Card Text: Reduce the Attack of an enemy minion by
1 until your next turn. <i>(Upgrades each turn!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass