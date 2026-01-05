"""Effect for Wailing Soul (FP1_016).

Card Text: <b>Battlecry: Silence</b> your other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)