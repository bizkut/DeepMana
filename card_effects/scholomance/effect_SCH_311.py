"""Effect for Animated Broomstick (SCH_311).

Card Text: <b>Rush</b>
<b>Battlecry:</b> Give your other minions <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1