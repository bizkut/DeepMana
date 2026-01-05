"""Effect for Wrenchcalibur (DAL_063).

Card Text: After your hero attacks, shuffle a Bomb into your [x]opponent's deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass