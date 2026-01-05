"""Effect for Doomguard (VAN_EX1_310).

Card Text: <b>Charge</b>. <b>Battlecry:</b> Discard two random cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass