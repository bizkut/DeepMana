"""Effect for Light of the New Moon (FIR_918).

Card Text: [x]Give a minion +3/+3.
<i>(Cast 3 spells to return this
to your hand when played.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3