"""Effect for Southsea Deckhand (CS2_146).

Card Text: Has <b>Charge</b> while you have a weapon equipped.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass