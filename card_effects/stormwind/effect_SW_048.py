"""Effect for Prismatic Jewel Kit (SW_048).

Card Text: [x]After a friendly minion loses
<b>Divine Shield</b>, give minions
in your hand  +1/+1.
Lose 1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1