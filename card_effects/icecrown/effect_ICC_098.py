"""Effect for Tomb Lurker (ICC_098).

Card Text: [x]<b>Battlecry:</b> Add a random
<b>Deathrattle</b> minion that died
this game to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass