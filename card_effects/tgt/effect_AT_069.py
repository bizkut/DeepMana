"""Effect for Sparring Partner (AT_069).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Give a
minion <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1