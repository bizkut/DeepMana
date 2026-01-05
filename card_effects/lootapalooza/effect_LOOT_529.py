"""Effect for Void Ripper (LOOT_529).

Card Text: <b>Battlecry:</b> Swap the
Attack and Health of all other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)