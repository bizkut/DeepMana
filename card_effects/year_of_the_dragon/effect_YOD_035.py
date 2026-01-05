"""Effect for Grand Lackey Erkh (YOD_035).

Card Text: After you play a <b>Lackey</b>, add a <b>Lackey</b> to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass