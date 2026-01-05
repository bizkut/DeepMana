"""Effect for Mossy Horror (CORE_GIL_124).

Card Text: <b>Battlecry:</b> Destroy all other minions with 2 or less Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()