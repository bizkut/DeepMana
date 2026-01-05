"""Effect for Magic Carpet (DAL_773).

Card Text: After you play a 1-Cost minion, give it +1 Attack and <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1