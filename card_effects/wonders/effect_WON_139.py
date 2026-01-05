"""Effect for Timeline Accelerator (WON_139).

Card Text: <b>Battlecry:</b> Draw a Mech.
It costs (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)