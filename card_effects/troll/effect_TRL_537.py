"""Effect for Da Undatakah (TRL_537).

Card Text: [x]<b>Battlecry:</b> Gain the
<b>Deathrattle</b> effects of
3 friendly minions that
died this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass