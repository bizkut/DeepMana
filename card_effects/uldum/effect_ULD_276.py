"""Effect for EVIL Totem (ULD_276).

Card Text: At the end of your turn,
add a <b>Lackey</b> to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass