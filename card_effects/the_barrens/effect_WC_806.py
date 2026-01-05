"""Effect for Floecaster (WC_806).

Card Text: Costs (2) less for each <b>Frozen</b> enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass