"""Effect for Pelagos (CORE_REV_250).

Card Text: [x]After you cast a spell 
on a friendly minion, set 
its Attack and Health to 
the higher of the two.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)