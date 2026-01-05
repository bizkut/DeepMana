"""Effect for Avenge (FP1_020).

Card Text: <b>Secret:</b> When one of your minions dies, give a random friendly minion +3/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3