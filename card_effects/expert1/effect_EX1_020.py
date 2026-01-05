"""Effect for Scarlet Crusader (EX1_020).

Card Text: <b>Divine Shield</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass