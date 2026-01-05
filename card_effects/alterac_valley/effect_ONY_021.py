"""Effect for Scale of Onyxia (ONY_021).

Card Text: Fill your board with 2/1 Whelps with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass