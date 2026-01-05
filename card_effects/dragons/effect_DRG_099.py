"""Effect for Kronx Dragonhoof (DRG_099).

Card Text: [x]<b>Battlecry:</b> Draw Galakrond.
If you're already Galakrond,
unleash a Devastation.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)