"""Effect for Relic Vault (REV_942).

Card Text: The next Relic you play this turn casts twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass