"""Effect for Archmage Vargoth (DAL_558).

Card Text: [x]At the end of your turn, cast
a spell you've cast this turn
<i>(targets are random)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass