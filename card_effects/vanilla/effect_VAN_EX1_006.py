"""Effect for Alarm-o-Bot (VAN_EX1_006).

Card Text: [x]At the start of your turn,
swap this minion with a
   random one in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass