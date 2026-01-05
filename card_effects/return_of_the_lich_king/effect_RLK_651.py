"""Effect for Crypt Keeper (RLK_651).

Card Text: <b>Taunt</b>. Costs (1) less for each Armor you have.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass