"""Effect for Twinbow Terrorcoil (TSC_071).

Card Text: [x]<b>Battlecry:</b> If you've cast a
spell while holding this, your
next spell casts twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass