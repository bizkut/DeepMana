"""Effect for Lady Anacondra (WC_006).

Card Text: Your Nature spells
cost (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass