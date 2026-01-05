"""Effect for Peon (BAR_022).

Card Text: [x]<b>Frenzy:</b> Add a random
spell from your class
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass