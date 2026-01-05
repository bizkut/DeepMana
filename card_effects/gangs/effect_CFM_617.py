"""Effect for Celestial Dreamer (CFM_617).

Card Text: [x]<b>Battlecry:</b> If you control a
minion with 5 or more
Attack, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5