"""Effect for Careful Bear (WORK_024t).

Card Text: <b>Taunt</b> At the start of your turn, if this is in your hand, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
