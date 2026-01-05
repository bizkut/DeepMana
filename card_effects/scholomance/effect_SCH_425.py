"""Effect for Doctor Krastinov (SCH_425).

Card Text: <b>Rush</b>
Whenever this attacks, give your weapon +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1