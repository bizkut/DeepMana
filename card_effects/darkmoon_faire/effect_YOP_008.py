"""Effect for Lightsteed (YOP_008).

Card Text: Your healing effects also give affected minions
+2 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)