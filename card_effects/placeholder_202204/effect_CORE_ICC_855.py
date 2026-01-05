"""Effect for Hyldnir Frostrider (CORE_ICC_855).

Card Text: <b>Battlecry:</b> <b>Freeze</b> your other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True