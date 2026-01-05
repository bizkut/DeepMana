"""Effect for Swiftscale Trickster (TSC_936).

Card Text: <b>Battlecry:</b> Your next spell this turn costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass