"""Effect for Obsidiansmith (TSC_942).

Card Text: [x]<b>Battlecry:</b> <b>Dredge</b>. If it's
a minion or a weapon,
give it +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1