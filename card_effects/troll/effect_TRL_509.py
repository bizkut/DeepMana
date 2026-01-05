"""Effect for Banana Buffoon (TRL_509).

Card Text: <b>Battlecry:</b> Add 2 Bananas to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass