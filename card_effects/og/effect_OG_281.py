"""Effect for Beckoner of Evil (OG_281).

Card Text: <b>Battlecry:</b> Give your C'Thun +2/+2 <i>(wherever it is).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2