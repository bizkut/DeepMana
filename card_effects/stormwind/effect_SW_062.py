"""Effect for Goldshire Gnoll (SW_062).

Card Text: [x]<b>Rush</b>
Costs (1) less for each
  other card in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass