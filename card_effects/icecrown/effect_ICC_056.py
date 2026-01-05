"""Effect for Cryostasis (ICC_056).

Card Text: Give a minion +3/+3 and <b>Freeze</b> it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3