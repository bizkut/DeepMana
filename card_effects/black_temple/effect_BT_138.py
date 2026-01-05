"""Effect for Bloodboil Brute (BT_138).

Card Text: <b>Rush</b>
Costs (1) less for each damaged minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass