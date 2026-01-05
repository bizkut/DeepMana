"""Effect for Skeletal Dragon (BT_341).

Card Text: [x]<b>Taunt</b>
At the end of your turn, add
a Dragon to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass