"""Effect for Ring of Courage (ONY_027).

Card Text: <b>Tradeable</b>
Give a minion +1/+1. Repeat for each enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1