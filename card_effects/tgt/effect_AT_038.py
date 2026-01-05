"""Effect for Darnassus Aspirant (AT_038).

Card Text: <b>Battlecry:</b> Gain an empty Mana Crystal.
<b>Deathrattle:</b> Lose a Mana Crystal.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass