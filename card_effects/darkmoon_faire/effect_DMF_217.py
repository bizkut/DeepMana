"""Effect for Line Hopper (DMF_217).

Card Text: Your <b>Outcast</b> cards cost (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass