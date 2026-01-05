"""Effect for Vilespine Slayer (UNG_064).

Card Text: <b>Combo:</b> Destroy a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()