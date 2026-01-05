"""Effect for Emeriss (GIL_128).

Card Text: <b>Battlecry:</b> Double the Attack and Health of all minions in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)