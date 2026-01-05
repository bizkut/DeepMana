"""Effect for Praise Galakrond! (DRG_030).

Card Text: [x]Give a minion +1 Attack.
<b>Invoke</b> Galakrond.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1