"""Effect for Herald of Light (TID_085).

Card Text: [x]<b>Battlecry:</b> If you've cast a
Holy spell while holding this,
restore #6 Health to all
friendly characters.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 6, source)