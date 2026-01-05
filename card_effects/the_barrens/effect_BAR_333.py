"""Effect for Kurtrus Ashfallen (BAR_333).

Card Text: [x]<b>Battlecry:</b> Attack the left and
right-most enemy minions.
<b>Outcast:</b> <b>Immune</b> this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass