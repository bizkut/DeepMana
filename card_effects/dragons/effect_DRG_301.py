"""Effect for Whispers of EVIL (DRG_301).

Card Text: Add a <b>Lackey</b> to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass