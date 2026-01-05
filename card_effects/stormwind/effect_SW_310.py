"""Effect for Counterfeit Blade (SW_310).

Card Text: [x]<b>Battlecry</b>: Get a copy
of a random friendly
<b>Deathrattle</b> minion
that died this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass