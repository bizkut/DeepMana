"""Effect for Mukla, Tyrant of the Vale (OG_122).

Card Text: <b>Battlecry:</b> Add 2 Bananas to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass