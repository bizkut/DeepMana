"""Effect for Dredger Staff (CORE_REV_338).

Card Text: [x]<b>Battlecry:</b> Give minions 
in your hand +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)