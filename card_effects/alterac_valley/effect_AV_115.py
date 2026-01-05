"""Effect for Amplified Snowflurry (AV_115).

Card Text: <b>Battlecry:</b> Your next Hero Power costs (0) and <b>Freezes</b> the target.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True