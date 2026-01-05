"""Effect for Bearshark (ICC_419).

Card Text: <b>Elusive</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass