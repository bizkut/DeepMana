"""Effect for Dread Corsair (NEW1_022).

Card Text: <b>Taunt</b>
Costs (1) less per Attack of your weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass