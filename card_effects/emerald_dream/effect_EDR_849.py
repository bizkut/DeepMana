"""Effect for Dreambound Raptor (EDR_849).

Card Text: After you play a minion, give it a random
<b>Bonus Effect</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1