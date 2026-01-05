"""Effect for Mindbreaker (CORE_ICC_902).

Card Text: Hero Powers are disabled.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass