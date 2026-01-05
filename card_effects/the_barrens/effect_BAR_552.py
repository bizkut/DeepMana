"""Effect for Scabbs Cutterbutter (BAR_552).

Card Text: [x]<b>Combo:</b> The next two
cards you play this turn
cost (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass