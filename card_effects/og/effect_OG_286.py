"""Effect for Twilight Elder (OG_286).

Card Text: At the end of your turn, give your C'Thun +1/+1 <i>(wherever it is).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1