"""Effect for Mana Giant (DRG_109).

Card Text: [x]Costs (1) less for each
card you've played this
game that didn't start
in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass