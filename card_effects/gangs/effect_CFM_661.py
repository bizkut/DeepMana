"""Effect for Pint-Size Potion (CFM_661).

Card Text: [x]Give all enemy minions
-3 Attack this turn only.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3