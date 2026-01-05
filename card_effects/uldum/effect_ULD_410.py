"""Effect for Scarlet Webweaver (ULD_410).

Card Text: <b>Battlecry:</b> Reduce the Cost of a random Beast in your hand by (5).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass