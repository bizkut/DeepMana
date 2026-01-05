"""Effect for Hope of Quel'Thalas (RLK_828).

Card Text: [x]After your hero attacks,
give your minions +1/+1
<i>(wherever they are).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1