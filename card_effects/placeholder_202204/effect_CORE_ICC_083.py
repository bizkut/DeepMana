"""Effect for Doomed Apprentice (CORE_ICC_083).

Card Text: Your opponent's spells cost (1) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass