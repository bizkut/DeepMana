"""Effect for Keeper of Uldaman (LOE_017).

Card Text: <b>Battlecry:</b> Set a minion's Attack and Health to 3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)