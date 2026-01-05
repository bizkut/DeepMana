"""Effect for Mana Cyclone (DAL_603).

Card Text: [x]<b>Battlecry:</b> For each spell
you've cast this turn, add
a random Mage spell
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass