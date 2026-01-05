"""Effect for Houndmaster Shaw (GIL_650).

Card Text: Your other minions have
<b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass