"""Effect for Heart of the Wild (AV_292).

Card Text: Give a minion +2/+2, then give your Beasts +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2