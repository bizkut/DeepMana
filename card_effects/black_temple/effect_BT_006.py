"""Effect for Evocation (BT_006).

Card Text: Fill your hand with random Mage spells.
They are <b>Temporary</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass