"""Effect for Sludge Slurper (DAL_433).

Card Text: <b>Battlecry:</b> Add a <b>Lackey</b> to your hand. <b>Overload:</b> (1)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass