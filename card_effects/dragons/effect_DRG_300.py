"""Effect for Fate Weaver (DRG_300).

Card Text: [x]<b>Battlecry:</b> If you've <b>Invoked</b>
twice, reduce the Cost of
cards in your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass