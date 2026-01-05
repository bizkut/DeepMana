"""Effect for Shan'do Wildclaw (SCH_607).

Card Text: [x]<b>Choose One -</b> Give Beasts
in your deck +1/+1; or
Transform into a copy
of a friendly Beast.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1