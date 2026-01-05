"""Effect for Herald of Shadows (TID_717).

Card Text: <b>Battlecry:</b> If you've cast a Shadow spell while holding this, steal 2 Health from a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)