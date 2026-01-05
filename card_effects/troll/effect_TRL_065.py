"""Effect for Zul'jin (TRL_065).

Card Text: [x]<b>Battlecry:</b> Cast all spells
you've played this game
<i>(targets chosen randomly)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass