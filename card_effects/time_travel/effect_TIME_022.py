"""Effect for Perennial Serpent (TIME_022).

Card Text: [x]<b>Rush</b>
Costs (4) less if a minion
is <b>Dormant</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass