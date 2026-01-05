"""Effect for Hit It Very Hard (ONY_023).

Card Text: Gain +10 Attack and "Can't attack heroes" this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 10
        target._max_health += 10