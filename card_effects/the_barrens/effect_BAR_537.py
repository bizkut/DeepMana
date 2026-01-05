"""Effect for Razormane Battleguard (BAR_537).

Card Text: The first <b>Taunt</b> minion you play each turn costs (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass