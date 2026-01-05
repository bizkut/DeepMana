"""Effect for Smoldering Strength (FIR_914).

Card Text: Give a friendly minion +{0}/+{0}.
<i>(Upgrades each turn,
but discards after {1}!)</i>1Give a friendly
minion +{0}/+{0}.
<i>(Discards this turn!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 0
        target._max_health += 0