"""Effect for Ready the Fleet (TLC_441).

Card Text: Give +1/+2 to a friendly minion and your other minions that share a type with it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1