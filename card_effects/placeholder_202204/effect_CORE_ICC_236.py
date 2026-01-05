"""Effect for Ice Breaker (CORE_ICC_236).

Card Text: Destroy any <b>Frozen</b> minion damaged by this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()