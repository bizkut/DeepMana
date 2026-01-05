"""Effect for Warsong Outrider (CORE_CS3_030).

Card Text: <b>Rush</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass