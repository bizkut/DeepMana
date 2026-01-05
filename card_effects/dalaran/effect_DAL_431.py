"""Effect for Swampqueen Hagatha (DAL_431).

Card Text: [x]<b>Battlecry:</b> Add a 5/5
Horror to your hand. Teach
it two Shaman spells.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass