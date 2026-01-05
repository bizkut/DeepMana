"""Effect for Glacial Shard (UNG_205).

Card Text: <b>Battlecry:</b> <b>Freeze</b> an enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True