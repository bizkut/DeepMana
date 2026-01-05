"""Effect for Tribute Dance (DINO_414).

Card Text: [x]Choose a minion.
Choose a different minion
to transform it into.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass