"""Effect for Attorney-at-Maw (MAW_025).

Card Text: <b>Choose One -</b> <b>Silence</b>
a minion; or Give a minion <b>Immune</b> this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1