"""Effect for Blessing of Authority (SCH_138).

Card Text: Give a minion +8/+8. It can't attack heroes this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 8
        target._max_health += 8