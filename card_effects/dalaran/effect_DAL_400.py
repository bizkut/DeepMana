"""Effect for EVIL Cable Rat (DAL_400).

Card Text: <b>Battlecry:</b> Add a <b>Lackey</b> to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass