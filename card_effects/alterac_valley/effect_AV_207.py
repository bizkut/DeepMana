"""Effect for Xyrella, the Devout (AV_207).

Card Text: [x]<b>Battlecry:</b> Trigger the
<b>Deathrattle</b> of every
friendly minion that
died this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass