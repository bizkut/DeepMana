"""Effect for Quel'dorei Fletcher (TIME_606).

Card Text: Your Hero Power costs
(0) while your hand has
3 or less cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass