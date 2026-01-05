"""Effect for Ethereal Peddler (KAR_070).

Card Text: <b>Battlecry:</b> If you're holding any cards from another class, reduce their Cost by (2).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass