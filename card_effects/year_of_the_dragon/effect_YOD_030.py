"""Effect for Licensed Adventurer (YOD_030).

Card Text: [x]<b>Battlecry:</b> If you control
a <b>Quest</b>, add a Coin
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass