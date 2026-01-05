"""Effect for Venomancer (CORE_ICC_032).

Card Text: <b>Poisonous</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass