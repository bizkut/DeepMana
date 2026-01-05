"""Effect for Jungle Panther (VAN_EX1_017).

Card Text: <b>Stealth</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass