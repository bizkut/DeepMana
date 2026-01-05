"""Effect for Iron Juggernaut (GVG_056).

Card Text: [x]<b>Battlecry and Deathrattle:</b>
Shuffle a Mine into your
opponent's deck. When drawn,
explode for 10 damage!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(10)


def deathrattle(game, source):
    pass