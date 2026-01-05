"""Effect for Techysaurus (DINO_409).

Card Text: [x]<b>Taunt</b>. Costs (1) less for
each card you played this
game that didn't start
in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass