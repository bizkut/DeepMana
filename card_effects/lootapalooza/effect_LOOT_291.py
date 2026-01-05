"""Effect for Shroom Brewer (LOOT_291).

Card Text: <b>Battlecry:</b> Restore #4 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)