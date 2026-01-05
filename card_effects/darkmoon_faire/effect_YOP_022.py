"""Effect for Mistrunner (YOP_022).

Card Text: <b>Battlecry:</b> Give a friendly minion +3/+3.
<b>Overload:</b> (1)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3