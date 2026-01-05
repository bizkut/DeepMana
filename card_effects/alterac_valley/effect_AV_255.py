"""Effect for Snowfall Guardian (AV_255).

Card Text: [x]<b>Battlecry:</b> <b>Freeze</b> all
other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True