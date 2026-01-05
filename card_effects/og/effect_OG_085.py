"""Effect for Demented Frostcaller (OG_085).

Card Text: After you cast a spell, <b>Freeze</b> a random enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True