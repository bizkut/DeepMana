"""Effect for Mogu Fleshshaper (ULD_169).

Card Text: [x]<b>Rush</b>. Costs (1) less for each
minion on the battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass