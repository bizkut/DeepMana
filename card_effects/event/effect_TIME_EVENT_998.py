"""Effect for Runi, Temporal Guardian (TIME_EVENT_998).

Card Text: [x]<b>Battlecry:</b> Send all minions
in your hand 2 turns into
the future. They return
with +5/+5.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2