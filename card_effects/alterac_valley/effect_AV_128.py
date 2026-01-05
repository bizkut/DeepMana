"""Effect for Frozen Mammoth (AV_128).

Card Text: This is <b>Frozen</b> until you
cast a Fire spell.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass