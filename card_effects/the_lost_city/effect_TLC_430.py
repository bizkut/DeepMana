"""Effect for Creature of the Sacred Cave (TLC_430).

Card Text: [x]At the end of your turn,
recast a random Holy spell
you cast this turn <i>(targets
this if possible)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass