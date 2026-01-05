"""Effect for Coldlight Oracle (VAN_EX1_050).

Card Text: <b>Battlecry:</b> Each player draws 2 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)