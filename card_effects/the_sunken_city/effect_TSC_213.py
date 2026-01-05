"""Effect for Queensguard (TSC_213).

Card Text: <b>Battlecry:</b> Gain +1/+1
for each spell you've cast this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1