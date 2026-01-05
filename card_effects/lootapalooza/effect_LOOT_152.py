"""Effect for Boisterous Bard (LOOT_152).

Card Text: <b>Battlecry:</b> Give your other minions +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)