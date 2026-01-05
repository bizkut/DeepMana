"""Effect for Crystalsmith Cultist (RLK_814).

Card Text: <b>Battlecry:</b> If you're
holding a Shadow spell, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1